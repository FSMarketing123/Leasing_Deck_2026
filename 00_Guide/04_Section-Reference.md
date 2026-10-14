# Section Reference — where everything lives

The site is one page: `05_Site/index.html` (in each deck). Open it in any text
editor (VS Code, BBEdit, TextEdit in plain-text mode) and use **Find** with the
search text in the table to jump to a section. Line numbers are for the master
and will drift as you edit.

| Order | Section | Find this text | Line (master) |
|------:|---------|----------------|------:|
| — | Intro curtain (logo + 0–100% counter) | `id="m-intro"` | 11 |
| — | Top navigation | `<nav id="nav">` | 23 |
| 1 | Hero | `══ HERO ══` | 37 |
| 2 | Franklin Advantage | `══ ADVANTAGE ══` | 102 |
| 3 | National Reach / Results | `══ RESULTS` | 128 |
| — | Kinetic scrolling words | `══ KINETIC TYPE BAND` | 318 |
| 4 | Team | `══ TEAM ══` | 324 |
| 5 | Platforms (5 pinned tabs) | `══ PLATFORMS ══` | 397 |
| 6 | Markets (logos + map) | `══ MARKET ══` | 564 |
| 7 | Featured Assignments (3D carousel) | `ASSIGNMENTS + PROCESS` | 707 |
| 8 | Process (5 pinned tabs, day→dusk photo) | `══ PROCESS ══` | 806 |
| 9 | Service Timeline | `══ SERVICE TIMELINE ══` | 885 |
| 10 | Live Website window | `══ LIVE WEBSITE ══` | 980 |
| 11 | Contact / CTA | `══ CTA ══` | 1055 |
| — | Footer (year updates itself) | `<footer>` | 1109 |

## Files

```
05_Site/
├── index.html              ← all words, links, photos, videos  (edit this most)
├── css/
│   ├── styles.css          ← layout, colors, sizes per section
│   ├── motion.css          ← animation styles (intro, cursor, rail, sheen)
│   └── fonts.css           ← Libre Baskerville + Open Sans (don't edit)
├── js/
│   ├── main.js             ← nav, carousel, video autoplay, process tabs
│   ├── motion.js           ← intro, smooth scroll, arrow-key/clicker nav, side rail
│   ├── theme.js            ← palette / headline style / spacing switch
│   └── vendor/vimeo-player.min.js
└── assets/
    ├── img/backgrounds/    ← hero, platforms, process day/dusk, timeline, textures
    ├── img/brand/          ← Franklin Street logo (white)
    ├── img/team/           ← headshots (also used in Contact)
    ├── img/logos/          ← partner + deal logos for the marquees
    ├── img/maps/           ← West Florida aerial
    ├── img/properties/     ← carousel photos
    ├── video/              ← self-hosted platform videos (.webm)
    └── fonts/
```

## Text formatting conventions

- **Green/teal italic word in a headline** → wrap it in `<em>…</em>`.
  `Partners, Not Just<br><em>Advisors.</em>`
- **Line break in a headline** → `<br>`.
- **Ampersand** → write `&amp;` (e.g. `Tampa Bay &amp; Florida`).
- Some elements carry small inline styles (`style="font-size: 15px"`). Copy an
  existing line when adding a new one so it matches.

---

## 1. Hero `#hero`

| Element | What to change | Notes |
|---|---|---|
| Eyebrow | text in `<div class="hero-eyebrow">` | keep short — one line |
| Headline | the three `<span class="word"><span>…</span></span>` lines | 2nd line is the green italic word. Each line animates up in turn |
| Subhead | `<p class="hero-sub">` | ~25 words |
| Award chips | each `<div class="award-chip">` (year `ay`, title + detail `al`) | 4 fit on one row |
| Stat card number | `<span class="counter" data-target="18">` | change `data-target` — it counts up from 0 |
| Stat card blocks | each `<div class="hsc-stat">` | 3 blocks |
| Background photo | `css/styles.css` → `.hero-map-bg` → `assets/img/backgrounds/hero-bg.jpg` | replace the file with the same name to avoid editing CSS. 2200×1400, under 800 KB |

## 2. Franklin Advantage `#advantage`

| Element | What to change |
|---|---|
| Headline / paragraphs | `adv-h2`, the two `adv-p` paragraphs |
| Value chips | each `<span class="val-chip">` |
| Video | the Vimeo number in `player.vimeo.com/video/1045159217?...` — swap just the number |

Videos autoplay muted when on screen and pause when you scroll away (handled by `js/main.js`).

## 3. National Reach `#results`

| Element | What to change |
|---|---|
| Headline | `<h2 class="res-h2">` |
| Six stat rows | each `<div class="res-row">` → category `res-row-cat`, number `<span class="big">`, label after it |
| US map image | `assets/img/backgrounds/results-us-map.jpg` |

The hidden SVG map inside `res-map-wrap` is legacy — leave it.

## Kinetic band `.kband`

Two rows of scrolling words. Each row repeats its phrases 4–6 times so the
loop is seamless — **change every repeat**, not just the first. `class="g"` =
green word, `class="o"` = outlined word, `<i>&#10022;</i>` = the ✦ divider.

## 4. Team `#team`

| Element | What to change |
|---|---|
| Intro sentence | `<p class="team-intro-text">` |
| People | each `<div class="team-card-mag">` → photo, `tc-name`, `tc-role` |
| Recognition row | each `<div class="accolade">` → `acc-year`, `acc-label`, `acc-title` |

Headshots: square, 1000×1000, face centered, under 200 KB, saved in
`assets/img/team/firstname-lastname.jpg`. If a face sits high or low, add
`style="object-position: center 20%"` on the `<img>` (see Michael Donley).
The layout is built for **3 people** per row; 2 or 4 also work.

## 5. Platforms `#platforms`

Pinned scroll section: on desktop the page "sticks" and each scroll step
advances one tab. Tabs and panels are matched by order.

| Element | What to change |
|---|---|
| Tab label | each `<button class="plat-tab">` → `plat-tab-cat` (small) and `plat-tab-title` |
| Panel media | Vimeo `<iframe class="js-vimeo" src="https://player.vimeo.com/video/NUMBER?...">` **or** `<video>` with `<source src="assets/video/name.webm">` |
| Panel copy | `plat-eyebrow`, `plat-h3`, `plat-p` |

To **add/remove a tab**: add/remove both the `<button class="plat-tab">` and its
`<div class="plat-panel">`, then renumber `data-panel="…"` and `goPlatform(…)`
from 0. Scroll length adjusts automatically.

## 6. Markets `#market`

| Element | What to change |
|---|---|
| Headline / paragraph | `market-h2`, `market-desc` |
| Partner logos | first `logo-marquee` → each `<div class="lm-chip"><img …></div>` |
| Deal logos | second `logo-marquee` |
| Map | `<img class="map-aerial">` + dots and labels |
| Map link | both `href="https://joom.ag/gDwd"` (map and green button) |
| Caption | `<div class="map-caption">` |

**Logos are listed twice in a row on purpose** — that's what makes the marquee loop
seamlessly. When you add or remove a logo, do it in **both halves**.
Logos: transparent PNG/SVG, ~600 px wide. If a logo is white or light, add `inv`
(`class="lm-chip inv"`) to darken it.

**Map dots** use percentages of the map image: `style="left:53.2%;top:64.7%;"`.
`map-dot sm` = small, `map-dot lg` = large lead city; pair each with a
`map-label` (`map-label lead` = the green one). Nudge numbers and refresh.

## 7. Featured Assignments `#assignments`

A 3D carousel. Each card is a `<div class="c3d" data-i="N">`:

```html
<div class="c3d" data-i="5">
  <div class="c3d-inner">
    <div class="c3d-img" style="padding:0;">
      <span class="c3d-tag">Grocery-Anchored</span>
      <img src="assets/img/properties/new-property.jpg" alt="New Property"
           style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;">
    </div>
    <div class="c3d-body">
      <div class="c3d-loc">Tampa, FL</div>
      <h3 class="c3d-title">New Property</h3>
      <p class="c3d-desc" style="color: rgb(0, 51, 73); font-weight: 400">One or two sentences on the result.</p>
      <div class="c3d-pills"><span class="c3d-pill" style="color: rgba(0, 51, 73, 0.6)">Tenant</span></div>
    </div>
  </div>
</div>
```

- Only the first card has `class="c3d active"`.
- `data-i` must run 0, 1, 2 … with no gaps.
- Add **one dot per card** below the carousel:
  `<button class="c3d-dot" onclick="setCard(5)"></button>`.
- The card count is detected automatically.
- Swap the `<img>` for a Vimeo iframe to show video (copy card 1).
- Long tenant lists: use `class="c3d-pills nowrap"` for smaller pills.
- Photos: 2000×1100 (landscape), under 600 KB.

## 8. Process `#process`

Pinned tabs like Platforms. Tabs are `<button class="proc-tab">`; panels are
`<div class="proc-panel" id="panel-N">`. Each panel has a big faded word
(`pp-num-large`), headline (`pp-h3`), paragraph (`pp-p`) and three
`pp-item`s with an icon and **bold title** in `<strong>`.

Background: `process-day.jpg` crossfades to `process-dusk.jpg` as you scroll.
Use two photos of the same view (2400×1350).

## 9. Service Timeline `#timeline`

Each week is a `<div class="tl-phase r">` with a number node, title
(`tl-phase-title`), badge (`tl-count`) and checklist (`<li class="tl-item">`).

- **Update the "N Actions" badge** when you add/remove items (the QC script checks this).
- 4+ items → two columns (`class="tl-list"`). 1–3 items → `class="tl-list single"`.

## 10. Live Website `#website`

The browser frame shows the **Buildout listings plugin** that franklinst.com uses — just the search,
filters, listings and map, without the franklinst.com header/footer:

`https://buildout.com/plugins/2f82fcd26667c4b0126d0084938ffa265f05fa4a/franklinst.com/inventory/?pluginId=0&iframe=true&embedded=true&cacheSearch=true&propertyType=2`

- `propertyType=2` = Retail. Remove it to show all property types.
- If franklinst.com changes plugins, open the for-lease page, inspect the listings frame, and copy its new address.
- The big green **View all listings on franklinst.com** button (`web-exit-btn`) and the bar's "Open franklinst.com ↗"
  link both open the full site in a new tab, so the deck stays open. Point them at a specific listing if wanted.
- Buildout shows its own cookie notice to first-time viewers; that's expected.

## 11. Contact `#cta`

| Element | What to change |
|---|---|
| Headline / paragraph | `cta-h2`, `cta-sub` |
| Consultation button | `href="mailto:A@Franklinst.com,B@Franklinst.com?cc=C@FranklinSt.com"` |
| Contact cards | each `<div class="contact-card">` → photo, role, name, email link, `tel:` links |
| Office | `os-label`, `os-addr` |

Phone links must be digits only: `href="tel:8138397300"`; the visible text can be formatted.

## Navigation & motion (automatic)

- **Top nav links** (`<ul class="nav-links">`) point to section ids — rename the
  label freely; keep the `href="#id"`.
- **Side rail** (dots on the right) and **arrow-key / clicker navigation** are
  built in `js/motion.js` (`var CH = [...]`). If you add a **new section**, add
  `['newid','Label']` there in page order.
- **Presenting live:** → / PageDown advance one "slide", ← / PageUp go back. A
  presentation clicker works.
- The logo marquees stop for viewers who have "reduce motion" turned on; the
  other animations always run.

## Look & feel switch

`js/theme.js` → `DECK_THEME` at the top:

```js
palette:   'teal'       // 'teal' | 'warm' | 'minimal'
typeStyle: 'editorial'  // 'editorial' | 'modern'
energy:    'refined'    // 'refined' | 'bold'
```

Preview any combination without editing: add
`?palette=warm&typeStyle=modern&energy=bold` to the address.

Brand colors live at the top of `css/styles.css` (`:root { --navy … }`).
