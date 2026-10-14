# Master Template Changelog

Changes to the Leasing template (`01_Templates/Leasing/`; was `01_Master-Template/`) that apply to every new deck. Newest first.

- 2026-10-14 · Folder reorganized: this system now lives in `Decks/Leasing/`; Capital Markets moved to `Decks/Capital Markets/`.

- 2026-10-14 · **Capital-Markets template v0.1 (draft)** created from Leasing v2.2, with a section-by-section
  build plan in its `TEMPLATE-INFO.md` and its own intake (`00_Guide/02_Intake-Questionnaire-Capital-Markets.md`).
  `new-deck.sh` now copies the intake that matches the chosen template.

- 2026-10-14 · **Leasing v2.2 locked** — snapshot `05_Archive/Template-Snapshots/Leasing_v2.2_2026-10-14/`.

- 2026-10-14 · Header logo now links to https://franklinst.com/ (new tab) instead of jumping to the top of the deck.

- 2026-10-14 · **Leasing v2.1** · Opening animation: replaced the lime layer + five "stair" panels with a navy
  screen where the geometric pattern draws outward from the logo as the counter runs, then dissolves into the hero.
  (`#m-intro .mi-pattern` in `css/motion.css`; `--p` set in `runIntro()` in `js/motion.js`.)

- 2026-10-14 · **Saved as the Leasing template v2.0** — moved `01_Master-Template/` to `01_Templates/Leasing/`;
  snapshot in `05_Archive/Template-Snapshots/Leasing_v2.0_2026-10-14/`. `new-deck.sh` takes an optional
  template name; QC compares each deck to its own template. Hero top line: dash removed.

- 2026-10-14 · Live Website callouts: 44px space on both sides of each column divider (text no longer touches lines).

- 2026-10-14 · Service Timeline widened from 1100px to 1240px (`.tl-track`).

- 2026-10-14 · Live Website: window now embeds only the Buildout listings plugin (search, filters, listings,
  map) instead of the whole franklinst.com page. Added a large green "View all listings on franklinst.com"
  button (new tab) with a note that the presentation stays open; browser-bar link relabeled.

- 2026-10-14 · Alignment: Service Timeline, Live Website and Hero now start on the same 1360px grid line as every
  other section (timeline list keeps its 1100px reading width). Rules at the end of `css/styles.css`.

- 2026-10-14 · National Reach: map back at the left page edge (bleeds off, so the cropped west coast isn't
  visible), enlarged to 60% width so it reaches toward the stats; removed the edge-fade wash.

- 2026-10-14 · Process: all five panel headings on one line; clear space between the big faded word and heading.
- 2026-10-14 · National Reach: map moved into the column beside the stats (stays close at every screen width;
  stacks above the stats on small screens). Partnerships / Deals labels: dash removed.

- 2026-10-14 · Section labels: bold, title first then the green dash (all 14 labels incl. hero).

- 2026-10-14 · Section labels (`.ey`, hero eyebrow): arrow icon replaced by a 40px green dash, labels in tracked
  Arial; light text on dark sections; removed duplicate arrow on "Drive · Passion · Commitment".
- 2026-10-14 · Process: tab labels larger and brighter (scale 12–14px with screen width so all five fit);
  "Performance & Reporting" heading on one line.

- 2026-10-14 · National Reach: same geometric pattern as Results That Speak (shared `#results::before` rule);
  US map blends with multiply so its white background no longer hides the pattern.

- 2026-10-14 · Results That Speak: added the geometric line pattern (from AdobeStock_294932998, converted to
  `assets/img/patterns/geometric-lines.svg`, 35 KB) as a faint teal backdrop that fades toward the edges.
  Strength = `opacity:0.085` on `#assignments::before` in `css/styles.css`.

- 2026-10-14 · Markets logo marquees: removed the edge fade so cards no longer look gray at the sides.

- 2026-10-14 · Kinetic band restyled: EB Garamond display line + tracked Arial caption line, thin
  green diamond dividers (no spin), hairline rules, scroll skew removed. EB Garamond loads from Google Fonts.
- 2026-10-14 · National Reach: removed the empty gap below the Advantage video, map now fades in at its edges
  and reveals from the top-right (under the video) instead of a hard block wiping in from the bottom.

- 2026-10-14 · Results That Speak: replaced the busy aerial photo backdrop with a cream gradient, faint
  blueprint grid and soft teal glow (photo kept in assets; restore note in `css/styles.css`). Tightened the
  gap between Results That Speak and Our Process from 240px to 48px (`PAD_OVERRIDES` in `js/theme.js`).

- 2026-10-14 · Rebuilt from the live single-file site (fstamparetail.netlify.app) into an
  editable folder: named assets, split CSS/JS, React "Tweaks" layer replaced by `js/theme.js`
  (same defaults). Carousel and tab counts now detected automatically instead of fixed at 5.
