#!/bin/bash
# new-deck.sh — start a new deck from a template in 01_Templates/.
#
#   bash tools/new-deck.sh "Westshore Plaza - Landlord Pitch"            (default template)
#   bash tools/new-deck.sh "Westshore Plaza - Landlord Pitch" Leasing    (pick a template)
#
# Creates 04_Decks/YYYY-MM_westshore-plaza-landlord-pitch/ with the working
# folders (intake, photos, video, data, copy, exports, feedback) and a fresh
# copy of the template website in 05_Site/.
set -e
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

if [ -z "$1" ]; then
  echo 'Usage: bash tools/new-deck.sh "Deck Name" [Template]'
  echo "Templates: $(ls "$ROOT/01_Templates" | tr '\n' ' ')"
  exit 1
fi
TEMPLATE="${2:-$(ls "$ROOT/01_Templates" | head -1)}"   # default: the first (or only) template
if [ ! -d "$ROOT/01_Templates/$TEMPLATE" ]; then
  echo "No template named \"$TEMPLATE\". Templates: $(ls "$ROOT/01_Templates" | tr '\n' ' ')"
  exit 1
fi

NAME="$1"
SLUG=$(echo "$NAME" | tr '[:upper:]' '[:lower:]' | sed -E 's/&/and/g; s/[^a-z0-9]+/-/g; s/^-+|-+$//g')
DEST="$ROOT/04_Decks/$(date +%Y-%m)_$SLUG"

if [ -e "$DEST" ]; then
  echo "Already exists: $DEST"
  exit 1
fi

cp -R "$ROOT/04_Decks/_DECK-TEMPLATE" "$DEST"
cp -R "$ROOT/01_Templates/$TEMPLATE/." "$DEST/05_Site/"
rm -f "$DEST/05_Site/.keep" "$DEST/05_Site/TEMPLATE-INFO.md"
# each template can have its own intake questions: 02_Intake-Questionnaire-<Template>.md
INTAKE="$ROOT/00_Guide/02_Intake-Questionnaire-$TEMPLATE.md"
[ -f "$INTAKE" ] || INTAKE="$ROOT/00_Guide/02_Intake-Questionnaire.md"
cp "$INTAKE" "$DEST/00_Intake/intake.md"

NAME_ESC=$(printf '%s' "$NAME" | sed 's/[&|\\]/\\&/g')
sed -i '' -e "s|{{DECK_NAME}}|$NAME_ESC|g" -e "s|{{TEMPLATE}}|$TEMPLATE|g" -e "s|{{CREATED}}|$(date +%Y-%m-%d)|g" \
  "$DEST/DECK-INFO.md" "$DEST/CHANGELOG.md"

echo "Created: $DEST  (template: $TEMPLATE)"
echo "Next: fill in 00_Intake/intake.md, then follow 00_Guide/01_Build-Guide.md"
