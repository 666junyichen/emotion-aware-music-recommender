# Scene Image API Setup

## Recommended Choice

Use **Pexels API first** for scene images.

Why:

- Free API key.
- Clear documentation.
- Good search quality for emotional scene queries.
- The API returns image URL, photographer name, photographer page, and source page.
- Rate limit is enough for this project: Pexels documents 200 requests per hour and 20,000 requests per month by default.

Official docs:

https://www.pexels.com/api/documentation/

## Can Codex Register the API Key?

No. API key registration needs your own account, email/login, and agreement to terms. I should not create accounts or accept terms on your behalf.

## How You Register a Free Pexels API Key

1. Open https://www.pexels.com/api/
2. Log in or create a free Pexels account.
3. Click the option to request/get an API key.
4. Create an application name such as `PulseScape`.
5. Copy the API key.
6. In PowerShell, run:

```powershell
$env:PEXELS_API_KEY="paste-your-key-here"
python scripts/fetch_scene_images.py pexels
```

If the script reaches Pexels but returns `HTTP Error 403: Forbidden`, the request is being rejected by Pexels. Common causes are:

- The copied API key is incomplete or has an extra hidden character.
- The Pexels API application is not fully approved or active yet.
- The account still needs email verification or terms acceptance.

The script sends the key in the standard `Authorization` header.

The script updates `music.json` with:

- `scene_image`
- `scene_source_url`
- `scene_attribution`
- `scene_license`
- `scene_query`

## Pixabay Alternative

Pixabay is also a good choice, especially because your music candidates are mostly from Pixabay. However, Pixabay pages may use bot protection for direct page access. The API is still suitable for images after you get a key.

Pixabay image URLs should not be used as permanent hotlinks. The fetch script now downloads returned images into:

```text
static/images/scenes/
```

Then it writes a local static path into `music.json`, such as:

```text
images/scenes/tear-away-pixabay.jpg
```

This is better for deployment because the app serves the images from the project instead of relying on temporary CDN URLs.

Official API docs:

https://pixabay.com/api/docs/

How to use:

1. Open https://pixabay.com/api/docs/
2. Log in or create a free Pixabay account.
3. Copy your API key from the docs page after login.
4. Run:

```powershell
$env:PIXABAY_API_KEY="paste-your-key-here"
python scripts/fetch_scene_images.py pixabay
```

## Good Scene Query Examples

- `rainy window melancholic piano`
- `quiet study room soft window light piano focus`
- `warm bedroom night lamp soft lullaby`
- `moonlit room soft curtains nocturne piano`
- `peaceful garden soft green light calming piano`
- `romantic window light piano violin gentle afternoon`
- `bright vintage piano room playful afternoon`
- `warm sunlight open sky joyful piano`

## Attribution

Pexels asks API users to show a prominent Pexels link and credit photographers when possible. Pixabay attribution is not required in the short license summary, but credit is appreciated. This project records attribution fields in `music.json` so the app or README can show them later.
