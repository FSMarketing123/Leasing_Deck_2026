#!/usr/bin/env python3
"""
unbundle.py — turn a single-file "bundled" landing page (the kind Claude Design /
Netlify drops export, ~20 MB with everything base64-embedded) into a clean,
editable website folder with real, human-named files.

    python3 tools/unbundle.py  <bundle.html | https://url>  <output-folder>

What it does
  1. Decodes every embedded asset (images, videos, fonts, scripts) to a real file
     and names it from where it is used (alt text, CSS selector, font family...).
  2. Rewrites the page so it points at those files.
  3. Splits the big <head> styles into css/fonts.css, css/styles.css, css/motion.css
     and the big end-of-page scripts into js/main.js, js/motion.js.
  4. Replaces the design-tool "Tweaks" React/Babel layer (4 MB of dev libraries
     that only exist to power the editor's palette panel) with js/theme.js, a
     tiny vanilla script that applies the same defaults. Pass --keep-react to
     leave the original React layer in place instead.

Safe to re-run: it only writes inside <output-folder>.
"""
import base64, gzip, html, json, os, re, shutil, sys, urllib.request, zlib

UUID = r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'
EXT = {'image/svg+xml': 'svg', 'image/png': 'png', 'image/jpeg': 'jpg', 'image/webp': 'webp',
       'image/gif': 'gif', 'video/webm': 'webm', 'video/mp4': 'mp4', 'text/jsx': 'jsx',
       'application/javascript': 'js', 'text/javascript': 'js', 'font/woff2': 'woff2',
       'font/woff': 'woff', 'text/css': 'css'}
HERE = os.path.dirname(os.path.abspath(__file__))

# Friendly names for CSS selectors that carry background images.
SELECTOR_NAMES = {
    '.hero-map-bg': 'backgrounds/hero-bg', '#platforms': 'backgrounds/platforms-bg',
    '#market::before': 'backgrounds/texture-overlay', '.shared-bg-wrap::before': 'backgrounds/assignments-bg',
    '.proc-bg-day': 'backgrounds/process-day', '.proc-bg-dusk': 'backgrounds/process-dusk',
    '#timeline': 'backgrounds/timeline-bg', '.res-map-bg': 'backgrounds/results-us-map',
}


def slug(s):
    s = html.unescape(s).lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')[:60] or 'asset'


def read_bundle(src):
    if re.match(r'https?://', src):
        with urllib.request.urlopen(src) as r:
            return r.read().decode('utf-8')
    return open(src, encoding='utf-8').read()


def block(s, kind):
    m = re.search(r'<script type="__bundler/%s">(.*?)</script>' % kind, s, re.S)
    return m.group(1) if m else None


def decode(entry):
    data = base64.b64decode(entry['data'])
    if entry.get('compressed'):
        try:
            data = gzip.decompress(data)
        except OSError:
            data = zlib.decompress(data, -15)
    return data


def name_assets(page, manifest):
    """Return {uuid: relative path under assets/ or js/}."""
    names, used = {}, set()

    def claim(uuid, path):
        base, ext = os.path.splitext(path)
        n, i = path, 2
        while n in used:
            n = '%s-%d%s' % (base, i, ext); i += 1
        used.add(n); names[uuid] = n

    # fonts: read each @font-face block
    for m in re.finditer(r'/\*\s*([\w-]+)\s*\*/\s*@font-face\s*\{(.*?)\}', page, re.S):
        subset, body = m.group(1), m.group(2)
        u = re.search(UUID, body)
        if not u or u.group(0) in names:
            continue
        fam = re.search(r"font-family:\s*'([^']+)'", body).group(1)
        style = re.search(r'font-style:\s*(\w+)', body).group(1)
        claim(u.group(0), 'assets/fonts/%s-%s-%s.woff2' % (slug(fam), style, subset))

    for uuid, entry in manifest.items():
        if uuid in names:
            continue
        mime, ext = entry['mime'], EXT.get(entry['mime'], 'bin')
        i = page.find(uuid)
        before = page[max(0, i - 600):i]
        after = page[i:i + 300]
        if mime.startswith('image/'):
            alt = re.match(UUID + r'"[^>]*?alt="([^"]*)"', after)
            if '<img' in before[-200:] and alt and alt.group(1):
                folder = 'logos' if 'lm-chip' in before[-120:] else (
                    'team' if 'tc-photo' in before[-120:] or 'cc-photo' in before[-120:] else
                    'properties' if 'c3d-img' in before[-400:] else
                    'maps' if 'map' in before[-200:] else 'images')
                claim(uuid, 'assets/img/%s/%s.%s' % (folder, slug(alt.group(1)), ext))
                continue
            sel = re.findall(r'([#.][\w-]+(?:::?[\w-]+)?)\s*\{[^{}]*$', before)
            if sel and sel[-1] in SELECTOR_NAMES:
                claim(uuid, 'assets/img/%s.%s' % (SELECTOR_NAMES[sel[-1]], ext))
            elif sel:
                claim(uuid, 'assets/img/backgrounds/%s.%s' % (slug(sel[-1]), ext))
            elif 'nav-logo' in before[-200:] or 'mi-logo' in before[-200:]:
                claim(uuid, 'assets/img/brand/franklin-street-logo.%s' % ext)
            else:
                claim(uuid, 'assets/img/images/image.%s' % ext)
        elif mime.startswith('video/'):
            ey = re.search(r'class="plat-eyebrow">\s*\d+\s*·\s*([^<]+)<', page[i:i + 2500])
            claim(uuid, 'assets/video/%s.%s' % (slug(ey.group(1)) if ey else 'video', ext))
        elif mime in ('application/javascript', 'text/javascript', 'text/jsx'):
            head = decode(entry)[:400].decode('utf-8', 'ignore')
            n = ('vimeo-player.min' if 'vimeo/player' in head else
                 'react.development' if 'react.development' in head else
                 'react-dom.development' if 'react-dom' in head else
                 'babel.min' if 'Babel' in head else
                 'tweaks-panel' if 'tweaks-panel' in head else 'script')
            claim(uuid, 'js/vendor/%s.%s' % (n, 'jsx' if ext == 'jsx' else 'js'))
        else:
            claim(uuid, 'assets/other/file.%s' % ext)
    return names


def apply_count_fixes(out):
    """The exported scripts hard-code 5 carousel cards and 5 tabs. Make them
    count the real items so decks with more or fewer still navigate correctly."""
    p = os.path.join(out, 'js', 'main.js')
    if os.path.exists(p):
        s = open(p).read().replace(
            "const TOTAL = 5;",
            "const TOTAL = document.querySelectorAll('#carousel3d .c3d').length; // counts the cards automatically")
        open(p, 'w').write(s)
    p = os.path.join(out, 'js', 'motion.js')
    if os.path.exists(p):
        s = open(p).read().replace(
            "function trackStops(track, n){\n  var sc",
            "function trackStops(track, n){\n  n = n || track.querySelectorAll('.plat-tab, .proc-tab').length || 1; // one stop per tab\n  var sc")
        for v in ('pt', 'pr', 'tr'):
            s = s.replace('trackStops(%s, 5)' % v, 'trackStops(%s)' % v)
        s = s.replace('cc < 4', "cc < $$('#carousel3d .c3d').length - 1")
        open(p, 'w').write(s)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    keep_react = '--keep-react' in sys.argv
    if len(args) != 2:
        print(__doc__); sys.exit(1)
    src, out = args
    s = read_bundle(src)
    manifest = json.loads(block(s, 'manifest'))
    page = json.loads(block(s, 'template'))
    names = name_assets(page, manifest)

    os.makedirs(out, exist_ok=True)
    for uuid, rel in names.items():
        p = os.path.join(out, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, 'wb') as f:
            f.write(decode(manifest[uuid]))

    # ── split head styles into css files ───────────────────────────────
    head_end = page.find('</head>')
    styles = list(re.finditer(r'<style( id="m-css")?>(.*?)</style>', page[:head_end], re.S))
    css_names = ['fonts.css', 'styles.css', 'motion.css']
    os.makedirs(os.path.join(out, 'css'), exist_ok=True)
    pieces, last = [], 0
    for k, m in enumerate(styles):
        fname = css_names[k] if k < len(css_names) else 'extra-%d.css' % k
        css = re.sub(UUID, lambda u: '../' + names.get(u.group(0), u.group(0)), m.group(2))
        with open(os.path.join(out, 'css', fname), 'w') as f:
            f.write(css.strip() + '\n')
        pieces.append(page[last:m.start()])
        pieces.append('<link rel="stylesheet" href="css/%s">' % fname)
        last = m.end()
    pieces.append(page[last:])
    page = ''.join(pieces)

    # ── split the two big end-of-body scripts into js files ────────────
    os.makedirs(os.path.join(out, 'js'), exist_ok=True)
    m = re.search(r'<script>\s*(// ── NAV ─.*?)</script>', page, re.S)
    if m:
        open(os.path.join(out, 'js', 'main.js'), 'w').write(m.group(1).strip() + '\n')
        page = page[:m.start()] + '<script src="js/main.js"></script>' + page[m.end():]
    m = re.search(r'<script id="m-js">(.*?)</script>', page, re.S)
    if m:
        open(os.path.join(out, 'js', 'motion.js'), 'w').write(m.group(1).strip() + '\n')
        page = page[:m.start()] + '<script src="js/motion.js"></script>' + page[m.end():]

    # ── replace the design-tool React "Tweaks" layer ───────────────────
    if not keep_react and 'TWEAK_DEFAULTS' in page:
        react_ids = [u for u, n in names.items()
                     if re.search(r'react|babel|tweaks-panel', n)]
        for u in react_ids:
            page = re.sub(r'<script[^>]*src="%s"[^>]*></script>\s*' % u, '', page)
            os.remove(os.path.join(out, names[u]))
        page = re.sub(r'<script type="text/babel">.*?</script>', '<script src="js/theme.js"></script>', page, flags=re.S)
        page = page.replace('<div id="tweaks-root"></div>\n', '')
        shutil.copy(os.path.join(HERE, 'theme.js'), os.path.join(out, 'js', 'theme.js'))

    page = re.sub(UUID, lambda u: names.get(u.group(0), u.group(0)), page)
    page = re.sub(r'\s+integrity="sha384-[^"]+"\s+crossorigin="anonymous"', '', page)
    open(os.path.join(out, 'index.html'), 'w').write(page)

    apply_count_fixes(out)
    vendor = os.path.join(out, 'js', 'vendor')
    if os.path.isdir(vendor) and not os.listdir(vendor):
        os.rmdir(vendor)
    print('Wrote %d assets + index.html to %s' % (len(names), out))
    for rel in sorted(names.values()):
        if os.path.exists(os.path.join(out, rel)):
            print('  ', rel)


if __name__ == '__main__':
    main()
