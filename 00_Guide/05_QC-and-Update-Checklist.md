# QC & Update Checklist

Copy this list into `07_Feedback/feedback-log.md` (or print it) for each version.

## 1. Automated check

- [ ] `python3 tools/check-deck.py 04_Decks/[deck-folder]/05_Site` shows **0 errors**
- [ ] Warnings reviewed (large images compressed, alt text added)
- [ ] "Sections still identical to master" list is intentional

## 2. Content

- [ ] Client / property names spelled correctly everywhere
- [ ] Numbers match across sections (hero "Active Florida Properties" ↔ map caption ↔ team copy)
- [ ] Every stat is current and has a source (platform stats, awards, SF, occupancy)
- [ ] Award years and titles match `02_Brand-Library/awards/awards-list.md`
- [ ] Team titles, emails, and phones match `03_Team-Library/team-roster.md`
- [ ] Spelling and grammar pass; no double spaces; consistent punctuation
- [ ] No leftover content from another deck or client
- [ ] Permission to show every partner and tenant logo
- [ ] Nothing confidential (rents, LOI terms) unless approved

## 3. Function — desktop (Chrome, then Safari)

- [ ] Intro curtain plays and clears (logo, 0–100% counter)
- [ ] Top nav links jump to the right sections; nav turns white on scroll
- [ ] → / ← keys (and a clicker) step through every section in order
- [ ] Side rail dots on the right highlight the current section and jump on click
- [ ] Hero counter counts up
- [ ] Advantage video plays muted on view, pauses when scrolled away
- [ ] Platforms: scrolling advances tabs 1→5; clicking a tab works; each video plays
- [ ] Markets: both logo rows scroll; map link opens the availability report
- [ ] Carousel: side arrows and dots move between every card; videos play on the active card
- [ ] Process: tabs advance on scroll; background shifts day → dusk
- [ ] Timeline: weeks light up in order; "N Actions" badges are right
- [ ] Live Website window loads franklinst.com; "Open ↗" works
- [ ] "Request a Consultation" opens an email to the right people
- [ ] Every email and phone link works
- [ ] Footer shows the current year

## 4. Function — phone and tablet

- [ ] iPhone (Safari) and Android (Chrome): no sideways scrolling
- [ ] Hero headline fits; stat card stacks below
- [ ] Carousel shows one card at a time with arrows
- [ ] Platforms/process tabs scroll sideways and switch panels on tap
- [ ] Videos play (tap to play is OK on phones)
- [ ] Text is readable without zooming

## 5. Presenting live

- [ ] Run through with the clicker on the presentation laptop
- [ ] Wi-Fi tested (Vimeo videos and the franklinst.com window need internet)
- [ ] Backup: PDF / screenshots in `06_Exports/` in case the venue has no internet

## 6. Release

- [ ] Approver sign-off recorded in `07_Feedback/feedback-log.md`
- [ ] Published; live URL in `DECK-INFO.md`
- [ ] Live URL tested in a private/incognito window
- [ ] `CHANGELOG.md` updated with version + date
- [ ] Reusable new assets copied to the libraries

---

## When updating an existing deck

- [ ] Change made in the deck's `05_Site/` (not the master — unless it applies to all decks)
- [ ] QC script re-run
- [ ] Re-published to the **same** Netlify site so the link doesn't change
- [ ] `CHANGELOG.md` entry: version, date, what changed, who asked
