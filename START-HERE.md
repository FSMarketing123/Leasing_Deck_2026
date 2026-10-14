# Franklin Street Decks — Leasing

_Capital Markets decks live next door in `../Capital Markets/`._

Everything for building and updating Franklin Street landing-page decks like
<https://fstamparetail.netlify.app/>.

## What's in this folder

| Folder | What it is |
|---|---|
| `00_Guide/` | How-to guides, intake questions, Claude prompts, checklists |
| `01_Templates/` | Saved deck templates. `Leasing/` is the approved retail leasing design. **Starting point for every deck — don't edit for a single deck.** |
| `02_Brand-Library/` | Logo, fonts, colors, partner/deal logos, awards list, backgrounds |
| `03_Team-Library/` | Headshots and the team roster (titles, emails, phones) |
| `04_Decks/` | One folder per deck. `_DECK-TEMPLATE` is the blank copied for each new one |
| `05_Archive/` | Finished or lost pursuits, moved out of `04_Decks` |
| `tools/` | Scripts: start a deck, preview, QC check, convert a design export |
| `CHANGELOG.md` | Changes to the Leasing template |
| `CLAUDE.md` | Instructions Claude reads automatically when working in this folder |

## The guides — read in this order

1. [Build Guide](00_Guide/01_Build-Guide.md) — the step-by-step process
2. [Intake Questionnaire](00_Guide/02_Intake-Questionnaire.md) — the questions to answer for each deck
3. [Claude Prompts](00_Guide/03_Claude-Prompts.md) — copy-paste prompts for each step
4. [Section Reference](00_Guide/04_Section-Reference.md) — where every element lives and how to edit it
5. [QC & Update Checklist](00_Guide/05_QC-and-Update-Checklist.md)
6. [Publish to Netlify](00_Guide/06_Publish-to-Netlify.md)
7. [Asset Specs](00_Guide/07_Asset-Specs.md) — image and video sizes

## The four commands

Open Terminal, then:

```bash
cd ~/Desktop/Decks/Leasing
```

| Do this | Command |
|---|---|
| Start a new deck | `bash tools/new-deck.sh "Deck Name"` |
| Preview a deck | `bash tools/preview.sh 04_Decks/[deck-folder]/05_Site` → open http://localhost:8080 |
| QC a deck | `python3 tools/check-deck.py 04_Decks/[deck-folder]/05_Site` |
| Convert a single-file design export | `python3 tools/unbundle.py export.html 01_Templates/Leasing-NEW` |

Or open this folder in Claude Code and ask in plain English — it knows these tools.

## Templates

| Template | Use it for | Version |
|---|---|---|
| `01_Templates/Leasing/` | Retail landlord-representation / leasing pitches | v2.2 · 2026-10-14 (locked) |

- Each template has a `TEMPLATE-INFO.md` with its version and design notes.
- Dated backups live in `05_Archive/Template-Snapshots/` — copy one back to roll a template back.
- **Add a new template type** (e.g. Investment Sales): copy `01_Templates/Leasing` to
  `01_Templates/Sales`, change it, update its `TEMPLATE-INFO.md`, then start decks with
  `bash tools/new-deck.sh "Deck Name" Sales`.

## The live site today

The current site is filed as `04_Decks/2026-10_tampa-retail-landlord-rep/`.
Its `05_Site` folder is an exact, editable rebuild of fstamparetail.netlify.app.
