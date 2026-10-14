# Asset Specs

Sizes match what the Leasing template uses. Save web images as **JPG (photos)**,
**PNG or SVG (logos)**, or **WebP** (either). Name files lowercase-with-dashes.

| Asset | Where it goes | Size (px) | Max file | Notes |
|---|---|---|---|---|
| Hero background | `assets/img/backgrounds/hero-bg.jpg` | 2200 × 1400 | 800 KB | skyline/aerial; a dark overlay is added on top |
| Platforms background | `backgrounds/platforms-bg.webp` | 1536 × 1024 | 500 KB | shown faded under white |
| Assignments/Process backdrop | `backgrounds/assignments-bg.jpg` | 2000 × 1250 | 500 KB | |
| Process day / dusk | `backgrounds/process-day.jpg`, `process-dusk.jpg` | 2400 × 1350 each | 700 KB | **same view**, day and dusk — they crossfade |
| Timeline background | `backgrounds/timeline-bg.jpg` | 1024 × 1024+ | 400 KB | heavily tinted navy |
| US map (Reach) | `backgrounds/results-us-map.jpg` | 2200 × 1760 | 300 KB | |
| Market map | `img/maps/west-florida-gulf-coast-aerial.jpg` | 1300 × 2000 (portrait) | 700 KB | portrait ratio 2112:3264; dots use % positions |
| Carousel property photo | `img/properties/name.jpg` | 2000 × 1100 | 600 KB | landscape; center the subject |
| Headshot | `img/team/firstname-lastname.jpg` | 1000 × 1000 | 200 KB | square, face centered, consistent background |
| Partner / deal logo | `img/logos/company-name.png` | ~600 wide | 200 KB | transparent background; dark logo preferred |
| Franklin Street logo | `img/brand/franklin-street-logo.png` | 2346 × 430 | — | white version; turned navy automatically on light sections |
| Platform video file | `assets/video/name.webm` | 1920 × 1080 | 10 MB | prefer Vimeo; muted loop |
| Vimeo video | link only | 16:9 | — | set to allow embedding on any domain |

## Quick ways to resize and compress (Mac)

- **Preview:** open image → Tools → Adjust Size → set width → File → Export →
  JPEG, quality slider ~70%.
- **Terminal (built-in `sips`):**

  ```bash
  sips -Z 2000 photo.jpg --out photo-web.jpg
  ```
- **Squoosh** (<https://squoosh.app>) in the browser for best compression / WebP.
- Or ask Claude: *"Resize everything in 01_Property-Photos/raw to web-ready per the asset specs."*

## Vimeo settings checklist

- Privacy → **Embed: Anywhere** (or add the netlify domain)
- Hide title, byline, portrait (the embed link already requests this)
- Upload at 1080p or higher
