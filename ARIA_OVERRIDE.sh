#!/bin/bash
echo "[ARIA] Cleaning old files..."
find . -type f ! -path "./.git/*" ! -path "./.gitignore" ! -path "./.github/*" ! -path "./ARIA_OVERRIDE.sh" -delete
echo "[ARIA] Copying new files into place..."
cp -r * ../aria-eternal-launch/
cd ../aria-eternal-launch
git add .
git commit -m "ARIA Final Upgrade Deployed"
git push origin main
echo "[ARIA] Deployment complete."
