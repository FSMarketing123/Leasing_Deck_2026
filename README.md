# Franklin Street — Leasing Deck System (2026)

Scroll-and-clicker landing-page decks for Franklin Street retail landlord representation,
based on fstamparetail.netlify.app.

**Start here:** [START-HERE.md](START-HERE.md)

| Folder | What it is |
|---|---|
| `00_Guide/` | Build guide, intake questions, Claude prompts, section reference, QC checklist, publishing, asset specs |
| `01_Templates/Leasing/` | Leasing template v2.2 (locked) — plain HTML/CSS/JS, no build step |
| `02_Brand-Library/` | Logo, fonts, colors, partner/deal logos, awards |
| `03_Team-Library/` | Headshots and team roster |
| `04_Decks/` | One folder per deck; `2026-10_tampa-retail-landlord-rep/05_Site` is the live site |
| `05_Archive/` | Template snapshots (v2.0, v2.2) |
| `tools/` | `new-deck.sh`, `preview.sh`, `check-deck.py`, `unbundle.py` |

## Preview locally

```bash
bash tools/preview.sh 04_Decks/2026-10_tampa-retail-landlord-rep/05_Site
```

Then open http://localhost:8080.

## Publish

Deploy `04_Decks/2026-10_tampa-retail-landlord-rep/05_Site` to Netlify (drag and drop, or connect this repo and set
the publish directory to that folder). See `00_Guide/06_Publish-to-Netlify.md`.
