#!/usr/bin/env python3
"""
check-deck.py — QC a deck website before you publish it.

    python3 tools/check-deck.py 04_Decks/2026-10_my-deck/05_Site

Checks
  ERRORS   missing image/video/font/css/js files, tabs that don't match their
           panels, carousel cards that don't match their dots, timeline
           "N Actions" badges that don't match the list, leftover placeholders
  WARNINGS images over 1 MB, videos over 10 MB, images without alt text,
           malformed email/phone links
  INFO     which sections are still word-for-word the same as the deck's
           template (so you can confirm that was intended), unused assets
"""
import html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = os.path.join(ROOT, '01_Templates')
errors, warns, infos = [], [], []


def read(p):
    return open(p, encoding='utf-8').read()


def text_of(fragment):
    t = re.sub(r'<(script|style)\b.*?</\1>', ' ', fragment, flags=re.S)
    t = re.sub(r'<[^>]+>', ' ', t)
    return re.sub(r'\s+', ' ', html.unescape(t)).strip()


def sections(page):
    out = {}
    for m in re.finditer(r'<section id="([\w-]+)".*?</section>', page, re.S):
        out[m.group(1)] = m.group(0)
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    site = os.path.abspath(sys.argv[1])
    index = os.path.join(site, 'index.html')
    if not os.path.exists(index):
        print('No index.html in', site); sys.exit(1)
    page = read(index)

    # ── referenced files ───────────────────────────────────────────
    refs = set()
    for m in re.finditer(r'(?:src|href)="([^"#:]+)"', page):
        refs.add(os.path.normpath(os.path.join(site, m.group(1))))
    for m in re.finditer(r'url\("?([^")]+?)"?\)', page):
        if not m.group(1).startswith(('data:', 'http', '#')):
            refs.add(os.path.normpath(os.path.join(site, m.group(1))))
    css_dir = os.path.join(site, 'css')
    for f in os.listdir(css_dir) if os.path.isdir(css_dir) else []:
        for m in re.finditer(r'url\("?([^")]+?)"?\)', read(os.path.join(css_dir, f))):
            if not m.group(1).startswith(('data:', 'http', '#')):
                refs.add(os.path.normpath(os.path.join(css_dir, m.group(1))))
    for r in sorted(refs):
        if not os.path.exists(r) and not r.endswith('.html'):
            errors.append('Missing file: %s' % os.path.relpath(r, site))

    # ── asset sizes / unused ──────────────────────────────────────
    for d, _, files in os.walk(os.path.join(site, 'assets')):
        for f in files:
            p = os.path.join(d, f)
            kb = os.path.getsize(p) // 1024
            rel = os.path.relpath(p, site)
            if f.startswith('.'):
                continue
            if rel.startswith('assets/img') and kb > 1024:
                warns.append('Large image (%d KB) — compress to under 1 MB: %s' % (kb, rel))
            if rel.startswith('assets/video') and kb > 10240:
                warns.append('Large video (%d MB) — consider Vimeo instead: %s' % (kb // 1024, rel))
            if os.path.normpath(p) not in refs and '/fonts/' not in rel:
                infos.append('Unused asset (safe to delete if not needed): %s' % rel)

    # ── structural counts ─────────────────────────────────────────
    def count(pat):
        return len(re.findall(pat, page))
    pairs = [
        ('Platform tabs', r'class="plat-tab[" ]', 'platform panels', r'class="plat-panel[" ]'),
        ('Process tabs', r'class="proc-tab[" ]', 'process panels', r'class="proc-panel[" ]'),
        ('Carousel cards', r'class="c3d[" ]', 'carousel dots', r'class="c3d-dot[" ]'),
    ]
    for a, pa, b, pb in pairs:
        na, nb = count(pa), count(pb)
        if na != nb:
            errors.append('%s (%d) do not match %s (%d)' % (a, na, b, nb))
    for i, m in enumerate(re.findall(r'class="c3d(?: active)?" data-i="(\d+)"', page)):
        if int(m) != i:
            errors.append('Carousel card #%d has data-i="%s" (should be %d)' % (i + 1, m, i))
    for m in re.finditer(r'tl-phase-title">(.*?)</h3>\s*<span class="tl-count">(\d+) Actions?</span>\s*</div>\s*<ul.*?</ul>', page, re.S):
        items = m.group(0).count('class="tl-item"')
        if items != int(m.group(2)):
            errors.append('Timeline "%s" says %s Actions but lists %d' % (text_of(m.group(1)), m.group(2), items))

    # ── placeholders / links / alt text ───────────────────────────
    body_text = text_of(page)
    for tok in ['TODO', 'TBD', 'XXX', 'Lorem', '[[', '{{', 'PLACEHOLDER']:
        if tok in body_text:
            i = body_text.find(tok)
            errors.append('Placeholder "%s" left in copy: …%s…' % (tok, body_text[max(0, i - 40):i + 40]))
    todos = [text_of(t) for t in re.findall(r'<span class="todo"[^>]*>.*?</span>', page, re.S)]
    if todos:
        errors.append('%d placeholders still to fill (class="todo"): %s' % (len(todos), '; '.join(todos[:12]) + (' …' if len(todos) > 12 else '')))
    for m in re.finditer(r'href="mailto:([^"]+)"', page):
        addrs = re.split(r'[,?&]|cc=|bcc=', m.group(1))
        for a in filter(None, addrs):
            if '@' in a and not re.match(r'^[\w.+-]+@[\w-]+\.[\w.]+$', a):
                warns.append('Odd email address in link: %s' % a)
    for m in re.finditer(r'href="tel:([^"]+)"', page):
        if not re.match(r'^\+?\d{10,11}$', m.group(1)):
            warns.append('Phone link should be digits only (e.g. tel:8138397300): %s' % m.group(1))
    for m in re.finditer(r'<img\b[^>]*>', page):
        if not re.search(r'alt="[^"]+"', m.group(0)) and 'mi-logo' not in page[max(0, m.start() - 40):m.start()]:
            warns.append('Image missing alt text: %s' % m.group(0)[:90])

    # ── compare with the deck's template (DECK-INFO.md "Template" row, default Leasing) ──
    tdirs = sorted(d for d in os.listdir(TEMPLATES) if os.path.isdir(os.path.join(TEMPLATES, d))) if os.path.isdir(TEMPLATES) else []
    tname = tdirs[0] if tdirs else 'Leasing'
    info = os.path.join(os.path.dirname(site), 'DECK-INFO.md')
    if os.path.exists(info):
        m = re.search(r'\|\s*Template\s*\|\s*([\w-]+)', read(info))
        if m: tname = m.group(1)
    MASTER = os.path.join(TEMPLATES, tname)
    if not os.path.isdir(MASTER):
        warns.append('Template "%s" not found in 01_Templates/' % tname)
    elif os.path.abspath(site) != os.path.abspath(MASTER) and os.path.exists(os.path.join(MASTER, 'index.html')):
        mine, master = sections(page), sections(read(os.path.join(MASTER, 'index.html')))
        same = [s for s in mine if s in master and text_of(mine[s]) == text_of(master[s])]
        changed = [s for s in mine if s not in same]
        infos.append('Sections customized for this deck: %s' % (', '.join(changed) or 'none'))
        infos.append('Sections still identical to the %s template: %s' % (tname, ', '.join(same) or 'none'))

    vimeo = sorted(set(re.findall(r'player\.vimeo\.com/video/(\d+)', page)))
    infos.append('Vimeo videos used: %s' % ', '.join(vimeo))
    links = sorted(set(re.findall(r'href="(https?://[^"]+)"', page)))
    infos.append('External links: %s' % ', '.join(links))

    print('\nQC report for', os.path.relpath(site, ROOT))
    print('=' * 60)
    for label, items in (('ERRORS', errors), ('WARNINGS', warns), ('INFO', infos)):
        print('\n%s (%d)' % (label, len(items)))
        for i in items:
            print('  •', i)
    print()
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
