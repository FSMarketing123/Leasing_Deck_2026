# Franklin Street Decks — instructions for Claude

This folder builds Franklin Street retail landlord-representation "decks": single-page,
scroll-and-clicker websites based on fstamparetail.netlify.app, published on Netlify.

## Layout
- `01_Templates/<Name>/` — saved templates (`Leasing` = the approved retail leasing deck, locked at v2.2; Capital Markets moved to `../Capital Markets/`; each has
  `TEMPLATE-INFO.md`). `new-deck.sh "Name" [Template]` copies one. Only edit a template when the user says the change
  is for **all future decks**; then log it in the root `CHANGELOG.md` and update the
  matching library file (`03_Team-Library/team-roster.md`, `02_Brand-Library/awards/awards-list.md`).
  Before a significant template change, snapshot it to `05_Archive/Template-Snapshots/<Name>_v<ver>_<date>/`.
- `04_Decks/<YYYY-MM_slug>/` — one deck. Edit only its `05_Site/`. Source material lives in
  `00_Intake/intake.md`, `04_Copy/copy-deck.md`, `01_Property-Photos/web-ready/`,
  `02_Video/videos.md`, `03_Data/`. Log feedback in `07_Feedback/feedback-log.md`,
  versions in the deck's `CHANGELOG.md`, status/URL in `DECK-INFO.md`.
- `00_Guide/04_Section-Reference.md` — how each section is built. Read it before editing.
- `00_Guide/07_Asset-Specs.md` — image sizes; resize with `sips` when files are too big.

## Tools
- New deck: `bash tools/new-deck.sh "Name"`
- QC: `python3 tools/check-deck.py <site-folder>` — run after every edit; fix all ERRORS.
- Preview: serve the site folder with `python3 -m http.server 8080 --directory <site-folder>`
  (run it in the background) and open http://localhost:8080 in the browser pane. The
  launch.json preview may fail on the Desktop folder because of macOS permissions.
- Convert a single-file export: `python3 tools/unbundle.py <file> <out-folder>`

## Rules for editing a site
- Keep the HTML structure and class names; change text, links, `src` paths and counts.
- Platforms/Process: tabs and panels match by order; renumber `data-panel` / `goPlatform(n)` /
  `goProcess(n)` / `panel-n` from 0.
- Carousel: `data-i` runs 0..n-1, only the first card has `active`, one `.c3d-dot` per card
  with `setCard(n)`. Card and tab counts are detected automatically by the scripts.
- Logo marquees list every logo twice (seamless loop) — edit both halves.
- Timeline `tl-count` "N Actions" must equal the number of `tl-item`s.
- New section → also add it to `var CH = [...]` in `js/motion.js` (side rail + clicker stops).
- Headline highlight word = `<em>`; ampersand = `&amp;`; phone links digits only.
- Never invent stats, awards, tenants, or contact details — mark unknowns `TBD` and ask.
- Show the user copy you wrote or changed before treating it as final.
- Don't publish or deploy without the user's go-ahead.
