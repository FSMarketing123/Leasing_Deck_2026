# Build Guide — creating a new deck

A "deck" here is a Franklin Street landing-page pitch like
<https://fstamparetail.netlify.app/>: a single scrolling website that presents
like slides (arrow keys / clicker) and can be sent as a link.

**Time:** about 2–4 hours once the intake and assets are gathered.

---

## The workflow at a glance

```
1 Start  →  2 Intake  →  3 Gather assets  →  4 Write copy  →  5 Build
                                                              ↓
           8 Archive  ←  7 Publish  ←  6 QC & review  ←───────┘
```

## Step 1 — Start a new deck folder

In Terminal (or ask Claude to do it):

```bash
cd ~/Desktop/Decks/Leasing && bash tools/new-deck.sh "Westshore Plaza - Landlord Pitch"
```

Capital markets decks are built the same way from `~/Desktop/Decks/"Capital Markets"`.

This creates `04_Decks/2026-10_westshore-plaza-landlord-pitch/` containing:

| Folder | Put here |
|---|---|
| `00_Intake/` | `intake.md` — the filled-in questionnaire, meeting notes, the RFP |
| `01_Property-Photos/raw/` | originals straight from the photographer / drone |
| `01_Property-Photos/web-ready/` | resized + compressed copies (see Step 3) |
| `02_Video/` | `videos.md` list of Vimeo links; any .webm/.mp4 files |
| `03_Data/` | Placer.ai exports, demographics, site plans, availability reports |
| `04_Copy/` | `copy-deck.md` — the final approved words, section by section |
| `05_Site/` | the website itself (a fresh copy of the master) |
| `06_Exports/` | PDF and screenshots of the finished deck |
| `07_Feedback/` | `feedback-log.md` — every comment and what was done about it |
| `DECK-INFO.md` | status, owner, live URL, dates |
| `CHANGELOG.md` | what changed in each version |

**Never edit `01_Templates/Leasing/` for a single deck.** It is the clean starting
point for every future deck. (See "Updating the master" below.)

## Step 2 — Intake

Open `00_Intake/intake.md` and answer the questions. It is organized in the
same order as the website, so every answer has a home. Two ways to do it:

1. **Fill it in yourself** — fastest if you already know the answers.
2. **Have Claude interview you** — paste Prompt 1 from `03_Claude-Prompts.md`.
   Claude asks one section at a time and writes the answers into the file.

Mark anything unknown as `TBD` — the QC script flags any `TBD` left in the
final site so nothing slips through.

## Step 3 — Gather and prepare assets

Use the libraries before asking for anything new:

- `02_Brand-Library/` — logo, fonts, partner logos, deal logos, backgrounds
- `03_Team-Library/` — headshots and `team-roster.md` (titles, emails, phones)

For new material, follow **`07_Asset-Specs.md`** (sizes and file types).
Name files in lowercase with dashes: `westshore-plaza-aerial.jpg`.

Video: upload to the Franklin Street Vimeo account and note the number from the
link (`vimeo.com/1045159217` → `1045159217`) in `02_Video/videos.md`. Vimeo is
preferred over video files — it keeps the site small and fast.

## Step 4 — Write the copy

Fill `04_Copy/copy-deck.md` with the final words for each section. Get it
approved **before** building — editing words in the copy deck is much easier
than editing them in the HTML. Keep headline lengths close to the master's so the
layout holds.

## Step 5 — Build

Option A — **with Claude Code (recommended):** open the `Decks` folder in Claude
and use Prompt 3 in `03_Claude-Prompts.md`. Claude reads the intake and copy deck,
edits `05_Site/index.html`, copies the assets in, and runs the QC check.

Option B — **by hand:** open `05_Site/index.html` and work top to bottom using
`04_Section-Reference.md`. Replace image files in `05_Site/assets/…`.

Preview while you work:

```bash
cd ~/Desktop/Decks/Leasing && bash tools/preview.sh 04_Decks/2026-10_westshore-plaza-landlord-pitch/05_Site
```

Open <http://localhost:8080> and refresh after each change. Press Ctrl+C in
Terminal to stop.

## Step 6 — QC and review

```bash
cd ~/Desktop/Decks/Leasing && python3 tools/check-deck.py 04_Decks/2026-10_westshore-plaza-landlord-pitch/05_Site
```

Fix every **ERROR**. Read each **WARNING**. The **INFO** list shows which sections
are still identical to the master — confirm that is intended.

Then work through `05_QC-and-Update-Checklist.md` (desktop, phone, clicker test,
every link and video). Log reviewer comments in `07_Feedback/feedback-log.md`.

## Step 7 — Publish

Follow `06_Publish-to-Netlify.md`. Record the live URL in `DECK-INFO.md` and save
a PDF / screenshots in `06_Exports/`.

## Step 8 — Wrap up

- Add a line to `CHANGELOG.md` (`v1.0 — sent to client`).
- New logos, headshots, or photos worth reusing → copy them into
  `02_Brand-Library/` or `03_Team-Library/`.
- When the pursuit is over, move the deck folder to `05_Archive/`.

---

## Updating an existing deck

1. Open the deck's folder, make changes in `05_Site/`.
2. Run the QC script.
3. Re-publish (drag `05_Site` to the same Netlify site — the URL stays the same).
4. Add a `CHANGELOG.md` entry (`v1.1 — updated occupancy to 94%`).

## Updating the Leasing template

Change the master only for things that should apply to **every future deck**:
new team member, new award, new platform stat, refreshed company copy.

1. Make the change in `01_Templates/Leasing/`.
2. Run `python3 tools/check-deck.py 01_Templates/Leasing`.
3. Note it in `CHANGELOG.md` at the top of the Decks folder.
4. Update `03_Team-Library/team-roster.md` or `02_Brand-Library/awards/awards-list.md` too.

Existing decks are **not** updated automatically. Copy the change into any live deck
that needs it.

## Starting from a new design-tool export

If a new version of the design is exported as one big single-file HTML (like the
original netlify site), convert it into an editable folder:

```bash
cd ~/Desktop/Decks/Leasing && python3 tools/unbundle.py ~/Downloads/new-export.html 01_Templates/Leasing-NEW
```

Compare it with the current master, then swap folders when you're happy.
