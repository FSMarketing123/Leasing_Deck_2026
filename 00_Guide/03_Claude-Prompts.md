# Claude Prompts — copy, paste, fill in the [brackets]

Open the **Decks** folder in Claude Code (desktop app → Code tab → choose
`~/Desktop/Decks/Leasing`). Claude reads `CLAUDE.md` in that folder automatically, so it
already knows the folder layout and rules. Replace `[deck-folder]` with the deck's
folder name, e.g. `2026-10_westshore-plaza-landlord-pitch`.

---

## Prompt 1 — Start a deck and run the intake interview

```
Start a new deck called "[Deck Name]" using tools/new-deck.sh.
Then interview me through 00_Intake/intake.md one section at a time
(A through O). For each section, show me the master's current answer,
ask what should change, and write my answers into the intake file.
Anything I don't know, mark TBD.
```

## Prompt 2 — Turn the intake into a copy deck

```
Read 04_Decks/[deck-folder]/00_Intake/intake.md and the current text in
05_Site/index.html. Write 04_Copy/copy-deck.md with the final wording for
every section, keeping each headline and paragraph close to the master's
length so the layout holds. Highlight anything you rewrote or invented
so I can approve it, and list open questions at the top.
```

## Prompt 3 — Build the site

```
Build the deck in 04_Decks/[deck-folder]/05_Site using the approved
04_Copy/copy-deck.md and the files in 01_Property-Photos/web-ready and
02_Video/videos.md. Follow 00_Guide/04_Section-Reference.md. Resize any image
that breaks 00_Guide/07_Asset-Specs.md. When done, run tools/check-deck.py,
fix every error, preview it, and give me a list of what changed per section.
```

## Prompt 4 — Swap one section quickly

```
In 04_Decks/[deck-folder]/05_Site, update the [Featured Assignments]
section: [add a card for Westshore Plaza, Tampa FL, tag "Grocery-Anchored",
photo 01_Property-Photos/web-ready/westshore.jpg, tenants Publix and
Starbucks, description "..."]. Keep the dots and numbering in sync and
run the QC check.
```

Other one-liners that work well:

- `Change the hero stat from 18 to 21 active properties in [deck-folder].`
- `Replace the Market Videos tab video with Vimeo 1234567890 in [deck-folder].`
- `Add Hines and Kin Properties to the partner marquee in [deck-folder] (both halves).`
- `Move map dots so Lakeland and Winter Haven show on the map in [deck-folder].`
- `Switch [deck-folder] to the warm palette and bold spacing.`

## Prompt 5 — QC review

```
QC 04_Decks/[deck-folder]/05_Site. Run tools/check-deck.py, then preview the
site at desktop and phone width and walk every section. Check spelling,
grammar, consistent numbers (hero vs. team vs. map caption), every link,
every email/phone, that every video plays, and arrow-key navigation through
all sections. Report problems as a table: section, problem, fix. Don't
change anything until I approve.
```

## Prompt 6 — Apply reviewer feedback

```
Here is feedback on [deck-folder]: [paste comments].
Log each comment in 07_Feedback/feedback-log.md, make the changes in
05_Site, run the QC check, and add a CHANGELOG.md entry for the new version.
```

## Prompt 7 — Prepare to publish

```
Get [deck-folder] ready to publish: run the QC check, take full-page
screenshots of each section into 06_Exports/screenshots, update DECK-INFO.md
status to "Ready to publish", and give me the Netlify drag-and-drop steps.
```

## Prompt 8 — Update the Leasing template

```
Update 01_Templates/Leasing for all future decks: [new award "2026 CoStar
Power Broker – Top Deal Awards Q3"]. Update every place it appears (hero
chips, recognition row), the matching library file (awards-list.md or
team-roster.md), run the QC check, and add an entry to the root CHANGELOG.md.
Then tell me which live decks in 04_Decks might need the same change.
```

## Prompt 9 — New design export

```
I exported a new version of the design to [~/Downloads/file.html]. Run
tools/unbundle.py into 01_Templates/Leasing-NEW, compare it to the current
01_Templates/Leasing section by section, and summarize what changed. Don't
replace the master until I confirm.
```

---

## Tips for good results

- **Be specific about the section** — use the names in `04_Section-Reference.md`.
- **Give numbers with sources** ("7.9M SF managed — per 2026 Q3 corporate stats").
- **Ask for a plan first** on big changes: add "show me the plan before editing."
- **Ask Claude to preview** — it can open the site in its built-in browser and check it.
- **Keep the master clean** — always name the deck folder in your request.
