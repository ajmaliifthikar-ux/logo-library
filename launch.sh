#!/bin/bash
# LogoLibrary Launch Script
# Usage: ./launch.sh YOUR_GITHUB_USERNAME

set -e

USERNAME="${1:-}"
if [ -z "$USERNAME" ]; then
  read -p "Enter your GitHub username: " USERNAME
fi

if [ -z "$USERNAME" ]; then
  echo "❌ GitHub username required"
  exit 1
fi

echo "🚀 Launching LogoLibrary for GitHub user: $USERNAME"

# ---- Push Logo_Library ----
echo ""
echo "📦 Pushing Logo_Library (core assets)..."
cd "$(dirname "$0")/Logo_Library"
git branch -M main 2>/dev/null || true
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "https://github.com/$USERNAME/logo-library.git"
else
  git remote add origin "https://github.com/$USERNAME/logo-library.git"
fi
echo "   Remote: $(git remote get-url origin)"
git push -u origin main || echo "   ⚠️ Push failed. Create the repo at https://github.com/new?repo_name=logo-library first, then re-run."

# ---- Push logo-explorer ----
echo ""
echo "🌐 Pushing logo-explorer (web dashboard)..."
cd "$(dirname "$0")/logo-explorer"
git branch -M main 2>/dev/null || true
if git remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin "https://github.com/$USERNAME/logo-library-web.git"
else
  git remote add origin "https://github.com/$USERNAME/logo-library-web.git"
fi
echo "   Remote: $(git remote get-url origin)"
git push -u origin main || echo "   ⚠️ Push failed. Create the repo at https://github.com/new?repo_name=logo-library-web first, then re-run."

# ---- Vercel Deploy ----
echo ""
echo "▲ Deploying to Vercel..."
if ! command -v vercel &> /dev/null; then
  echo "   ⚠️ Vercel CLI not found. Install with: npm i -g vercel"
  exit 1
fi

if ! vercel whoami >/dev/null 2>&1; then
  echo "   🔑 Please log in to Vercel:"
  vercel login
fi

cd "$(dirname "$0")/logo-explorer"
vercel --prod --yes

echo ""
echo "✅ Done! Your library is live."
echo ""
echo "   GitHub (Core):    https://github.com/$USERNAME/logo-library"
echo "   GitHub (Web):     https://github.com/$USERNAME/logo-library-web"
echo ""
