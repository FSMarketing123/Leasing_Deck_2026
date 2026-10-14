# Publish to Netlify

The original deck is hosted on Netlify at `fstamparetail.netlify.app`. Each deck
is its own Netlify site with its own address.

## First publish (drag and drop — no code)

1. Run the QC check and fix all errors.
2. Sign in at <https://app.netlify.com> with the team account.
3. Go to **Sites → Add new site → Deploy manually**.
4. Drag the deck's **`05_Site` folder** (the folder that holds `index.html`)
   onto the upload area.
5. When it finishes, open **Site configuration → Change site name** and pick a
   clear name, e.g. `fs-westshore-plaza` → `fs-westshore-plaza.netlify.app`.
6. Open the link in a private/incognito window and test it.
7. Paste the URL into `DECK-INFO.md`.

## Updating a published deck (same link)

1. In Netlify, open the deck's site → **Deploys**.
2. Drag the updated `05_Site` folder onto the **"Drag and drop your site output
   folder here"** box at the bottom of the Deploys page.
3. The same URL now shows the new version. Old versions stay listed under
   Deploys — click one and **Publish deploy** to roll back.

## Updating the original site (fstamparetail.netlify.app)

Use `04_Decks/2026-10_tampa-retail-landlord-rep/05_Site`, which is the
editable rebuild of that site. Drag it onto the fstamparetail site's Deploys
page. This replaces the old single-file bundle with the folder version — it
looks and works the same, and loads faster.

## Optional: publish from Terminal

```bash
npm install -g netlify-cli
netlify login
cd ~/Desktop/Decks/Leasing/04_Decks/[deck-folder]/05_Site
netlify deploy --prod
```

The first time, choose "Link to existing site" or "Create & configure a new site".

## Before you send the link

- Private decks: Netlify sites are public to anyone with the link. For
  password protection use Netlify's **Site configuration → Access control** (paid
  plans), or don't put confidential numbers on the page.
- Size: keep the site under ~50 MB; use Vimeo for long videos.
- Search engines: if the deck shouldn't show up in Google, add this line inside
  `<head>` in `index.html`:

  ```html
  <meta name="robots" content="noindex, nofollow">
  ```
