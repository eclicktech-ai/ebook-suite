#!/usr/bin/env bash
# Push each commit in origin/main..HEAD as its own `git push` (oldest first).
#
# WHAT THIS FIXES:
#   One `git push` that would send MULTIPLE commits in a single pack — sometimes
#   that combined pack is huge. Pushing commit-by-commit can reduce per-push size.
#
# WHAT THIS DOES *NOT* FIX:
#   GitHub also rejects a push when a SINGLE commit's pack still exceeds ~2 GiB on
#   receive. In that case splitting pushes is useless — you must split the COMMIT
#   (smaller commits), use Git LFS, or remove/shrink large blobs. See README.md.
#
# Usage (from ebook-suite repo root):
#   bash scripts/push-commits-one-by-one.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

git fetch origin

RANGE="origin/main..HEAD"
COUNT="$(git rev-list --count "$RANGE")"
if [[ "$COUNT" -eq 0 ]]; then
  echo "nothing to push (already up to date with origin/main)"
  exit 0
fi

cat <<'EOF'
Note: Per-commit push helps when the problem was one push carrying many commits.
If GitHub still says "pack exceeds maximum allowed size (2.00 GiB)" for ONE commit,
this script cannot fix that — split that commit or use Git LFS (see README).

EOF

echo "Pushing $COUNT commit(s) one by one (oldest first)..."
while IFS= read -r rev; do
  echo ""
  echo "---- $(git log -1 --oneline "$rev") ----"
  git push origin "$rev:refs/heads/main"
done < <(git rev-list --reverse "$RANGE")

echo ""
echo "Done. Verify: git status -sb && git log -1 --oneline origin/main"
