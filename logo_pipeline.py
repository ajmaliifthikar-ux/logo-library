#!/usr/bin/env python3
"""
LogoLibrary Auto-Pipeline Orchestrator
======================================
Single entry point that manages the entire flow:
  1. Figma queue processing (with rate-limit backoff)
  2. Asset organization & metadata indexing
  3. Git auto-commit
  4. Cloudinary CDN sync

Prevents duplicate processes via PID files.
Usage: python3 logo_pipeline.py [--figma] [--git] [--cdn]
"""

import os, sys, json, time, sqlite3, subprocess, signal, argparse
from pathlib import Path

BASE = Path(__file__).parent.resolve()
PID_DIR = BASE / ".pipeline_pids"
PID_DIR.mkdir(exist_ok=True)

FIGMA_QUEUE = BASE / "figma_queue.txt"
FIGMA_PROCESSED = BASE / "figma_processed.txt"
LOGOS_DIR = BASE / "Logo_Library" / "Assets"
META_PATH = BASE / "Logo_Library" / "metadata.json"
DB_PATH = BASE / "Logo_Library" / "library_index.db"

def pid_file(name): return PID_DIR / f"{name}.pid"

def is_running(name):
    pf = pid_file(name)
    if not pf.exists(): return False
    try:
        pid = int(pf.read_text().strip())
        os.kill(pid, 0)
        return True
    except (OSError, ValueError):
        pf.unlink(missing_ok=True)
        return False

def start_daemon(name, cmd):
    if is_running(name):
        print(f"[{name}] Already running (PID {pid_file(name).read_text().strip()})")
        return
    print(f"[{name}] Starting...")
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    pid_file(name).write_text(str(proc.pid))
    print(f"[{name}] Started with PID {proc.pid}")

def stop_daemon(name):
    pf = pid_file(name)
    if not pf.exists():
        print(f"[{name}] Not running")
        return
    try:
        pid = int(pf.read_text().strip())
        os.kill(pid, signal.SIGTERM)
        print(f"[{name}] Stopped PID {pid}")
    except Exception as e:
        print(f"[{name}] Error stopping: {e}")
    pf.unlink(missing_ok=True)

def update_metadata():
    """Rebuild metadata.json from the Assets folder."""
    if not LOGOS_DIR.exists():
        print("[metadata] Assets dir not found, skipping")
        return

    metadata = {}
    for cat_dir in LOGOS_DIR.iterdir():
        if not cat_dir.is_dir(): continue
        for brand_dir in cat_dir.iterdir():
            if not brand_dir.is_dir(): continue
            key = brand_dir.name.lower().replace(" ", "-")
            assets = []
            for f in sorted(brand_dir.iterdir()):
                if f.suffix.lower() not in (".svg", ".png"): continue
                parts = f.stem.split("-")
                variant = parts[-1] if parts[-1] in ("icon", "wordmark", "full", "default") else "default"
                assets.append({
                    "type": variant,
                    "format": f.suffix.replace(".", ""),
                    "path": str(f.relative_to(BASE / "Logo_Library")).replace("\\", "/")
                })
            if assets:
                metadata[key] = {
                    "brand_name": brand_dir.name.replace("-", " ").title(),
                    "category": cat_dir.name.replace("_", " ").replace(" and ", " & "),
                    "tags": [key, "logo"],
                    "assets": assets
                }

    META_PATH.write_text(json.dumps(metadata, indent=2))
    print(f"[metadata] Indexed {len(metadata)} brands, {sum(len(b['assets']) for b in metadata.values())} assets")

def update_sqlite():
    """Rebuild SQLite FTS5 index."""
    if not META_PATH.exists(): return
    data = json.loads(META_PATH.read_text())
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS logos_fts")
    c.execute("CREATE VIRTUAL TABLE logos_fts USING fts5(brand_name, category, tags, path, content='')")
    for key, brand in data.items():
        for asset in brand["assets"]:
            c.execute(
                "INSERT INTO logos_fts (brand_name, category, tags, path) VALUES (?,?,?,?)",
                (brand["brand_name"], brand["category"], ",".join(brand["tags"]), asset["path"])
            )
    conn.commit()
    conn.close()
    print(f"[sqlite] FTS5 index rebuilt with {len(data)} brands")

def git_auto_commit():
    """Auto-commit changes in Logo_Library."""
    lib = BASE / "Logo_Library"
    result = subprocess.run(
        ["git", "-C", str(lib), "status", "--porcelain"],
        capture_output=True, text=True
    )
    if not result.stdout.strip():
        return  # nothing to commit
    subprocess.run(["git", "-C", str(lib), "add", "."], check=False)
    subprocess.run(
        ["git", "-C", str(lib), "commit", "-m", f"auto: sync assets @ {time.strftime('%Y-%m-%d %H:%M')}"],
        check=False
    )
    print("[git] Auto-committed new assets")

def run_figma_processor():
    """Run the Figma extractor with queue management."""
    if not FIGMA_QUEUE.exists():
        print("[figma] No queue file found")
        return
    lines = [l.strip() for l in FIGMA_QUEUE.read_text().splitlines() if l.strip()]
    processed = set()
    if FIGMA_PROCESSED.exists():
        processed = set(FIGMA_PROCESSED.read_text().splitlines())

    pending = [l for l in lines if l not in processed]
    if not pending:
        print("[figma] No pending Figma URLs")
        return

    print(f"[figma] Processing {len(pending)} queued URLs...")
    # Use master_processor.py if available
    proc_script = BASE / "master_processor.py"
    if proc_script.exists():
        subprocess.run([sys.executable, str(proc_script)], cwd=str(BASE))
    else:
        print("[figma] master_processor.py not found")

def main():
    parser = argparse.ArgumentParser(description="LogoLibrary Pipeline Orchestrator")
    parser.add_argument("--figma", action="store_true", help="Process Figma queue")
    parser.add_argument("--git", action="store_true", help="Auto-commit to git")
    parser.add_argument("--cdn", action="store_true", help="Sync to Cloudinary CDN")
    parser.add_argument("--index", action="store_true", help="Rebuild metadata + SQLite")
    parser.add_argument("--all", action="store_true", help="Run full pipeline")
    parser.add_argument("--stop", action="store_true", help="Stop all background tasks")
    parser.add_argument("--status", action="store_true", help="Show running tasks")
    parser.add_argument("--daemon", action="store_true", help="Run as continuous background watcher")
    args = parser.parse_args()

    if args.status:
        for name in ("figma", "git", "cdn", "watcher"):
            status = "🟢 running" if is_running(name) else "🔴 stopped"
            print(f"  {name:12} {status}")
        return

    if args.stop:
        for name in ("figma", "git", "cdn", "watcher"):
            stop_daemon(name)
        return

    if args.daemon:
        print("[watcher] Starting continuous pipeline watcher...")
        while True:
            try:
                update_metadata()
                update_sqlite()
                git_auto_commit()
                run_figma_processor()
                time.sleep(300)  # 5 minute intervals
            except KeyboardInterrupt:
                print("\n[watcher] Stopping...")
                break
            except Exception as e:
                print(f"[watcher] Error: {e}")
                time.sleep(60)
        return

    if args.all or args.index:
        update_metadata()
        update_sqlite()

    if args.all or args.figma:
        run_figma_processor()

    if args.all or args.git:
        git_auto_commit()

    if args.all or args.cdn:
        sync_script = BASE / "cloudinary_sync.sh"
        if sync_script.exists():
            subprocess.run(["bash", str(sync_script)], cwd=str(BASE))
        else:
            print("[cdn] cloudinary_sync.sh not found")

    if not any([args.all, args.figma, args.git, args.cdn, args.index, args.daemon, args.status, args.stop]):
        parser.print_help()

if __name__ == "__main__":
    main()
