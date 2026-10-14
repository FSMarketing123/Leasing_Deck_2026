#!/bin/bash
# preview.sh — view a deck's website on your computer.
#
#   bash tools/preview.sh 04_Decks/2026-10_my-deck/05_Site
#   bash tools/preview.sh                      (previews the Leasing template)
#
# Then open http://localhost:8080 in your browser. Press Ctrl+C to stop.
# (Opening index.html by double-clicking mostly works too, but the Vimeo
# videos and the live franklinst.com window need a real local server.)
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${1:-01_Templates/Leasing}"
case "$SITE" in /*) ;; *) SITE="$ROOT/$SITE" ;; esac
PORT="${2:-8080}"

echo "Serving $SITE"
echo "Open http://localhost:$PORT"
python3 -m http.server "$PORT" --directory "$SITE"
