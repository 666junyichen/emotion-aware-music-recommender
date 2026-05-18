# Public Music and Scene Image Sourcing

This document tracks the next step for replacing demo audio and placeholder scene images with public-safe media.

## Current Decision

Do not publish the original project audio unless each file has a clear redistribution license. The live demo currently uses generated fallback audio when the original track file is not present.

For the next public version:

1. Download 10-20 tracks from public-safe sources.
2. Save MP3 files under `static/audio/public/`.
3. Add the track metadata to `music.json`.
4. Record `source_url`, `license`, and `attribution` for every track.
5. Replace placeholder scene images with licensed image URLs from Pexels or Pixabay.

## Downloaded Public Audio

The project now includes 10 real MP3 files in:

```text
static/audio/public/
```

These tracks have been added to `music.json` with `filepath`, `source_url`, `license`, and `attribution`.

Downloaded files:

| File | Track | License recorded in `music.json` |
| --- | --- | --- |
| `calm-piano-background-music-free.mp3` | Calm Piano Background Music Free | CC BY 4.0 |
| `melancholic-piano-music.mp3` | Melancholic Piano Music | CC BY 4.0 |
| `the-entertainer-piano.mp3` | The Entertainer Song | CC BY 4.0 |
| `chopin-nocturne-op-9-no-2.mp3` | Chopin Nocturne op.9 no.2 | Public Domain Mark 1.0 |
| `ode-to-joy-melody-piano.mp3` | Ode To Joy Melody Piano | CC BY 4.0 |
| `mozart-piano-concerto-23-adagio.mp3` | Mozart Piano Concerto 23 | CC BY 4.0 |
| `free-calming-music.mp3` | Free Calming Music | CC BY 4.0 |
| `twinkle-twinkle-little-star-piano.mp3` | Twinkle Twinkle Little Star Song | CC BY 4.0 |
| `traumerei-piano-music.mp3` | Traumerei - Piano Music | Public Domain Mark 1.0 |
| `salut-d-amour.mp3` | Salut D Amour | CC BY 3.0 |
 
The app can now play these MP3 files directly. Original project audio records remain in the library but still fall back to generated demo audio until their licenses are reviewed.

## Recommended Music Source

Pixabay Music is the best first source for this project because track pages clearly show:

- Track title.
- Artist.
- Duration.
- Media type MP3.
- Download action.
- "Free for use under the Pixabay Content License."

Pixabay's license summary says users may use content for free, attribution is not required though appreciated, and content may be modified, subject to prohibited uses such as selling/distributing unmodified content on a standalone basis.

Official license page:

https://pixabay.com/service/license-summary/

## Candidate Tracks

The structured candidate list is stored in:

`data/public_music_candidates.json`

Recommended first batch:

| Title | Artist | Suggested mood | Source |
| --- | --- | --- | --- |
| Please Calm My Mind | music_for_video | Calm | https://pixabay.com/music/beautiful-plays-please-calm-my-mind-125566/ |
| Please Calm My Mind | Onetent | Calm | https://pixabay.com/music/ambient-please-calm-my-mind-149224/ |
| Calm Ambient | QuietPhase | Recovery | https://pixabay.com/music/meditationspiritual-calm-ambient-491577/ |
| Calm Nature | AtlasAudio | Calm | https://pixabay.com/music/solo-piano-calm-nature-510279/ |
| Good Night - Lofi Cozy Chill Music | FASSounds | Calm | https://pixabay.com/music/good-night-160166/ |
| Lofi Study - Calm Peaceful Chill Hop | FASSounds | Focused | https://pixabay.com/music/lofi-study-112191/ |
| Tasty - Chill Lofi Vibe | FASSounds | Focused | https://pixabay.com/music/beats-tasty-chill-lofi-vibe-242105/ |
| Focus Zone - Relax Mellow Lofi Music | FASSounds | Focused | https://pixabay.com/music/beats-focus-zone-relax-mellow-lofi-music-259701/ |
| Coffee Chill Out | RomanBelov | Calm | https://pixabay.com/music/beats-coffee-chill-out-15283/ |
| Night Street (Relaxed Vlog) | Ashot_Danielyan | Sad | https://pixabay.com/music/beats-relaxed-vlog-night-street-131746/ |
| Once In Paris | Pumpupthemind | Happy | https://pixabay.com/music/search/pumpupthemind/ |
| Morning Garden - Acoustic Chill | folk_acoustic | Happy | https://pixabay.com/music/search/morning%20garden%20acoustic%20chill/ |

For rows that currently point to a search page, open the exact track page before downloading and replace the `source_url` with that exact page URL.

## How to Add Downloaded Music

Create this folder:

```text
static/audio/public/
```

Rename downloaded files using simple lowercase names:

```text
please-calm-my-mind.mp3
calm-ambient.mp3
lofi-study-calm-peaceful-chill-hop.mp3
```

Then update `music.json`:

```json
{
  "id": "please-calm-my-mind",
  "title": "Please Calm My Mind",
  "artist": "music_for_video",
  "emotion": "Calm",
  "genre": "relaxing piano",
  "vocal_type": "instrumental",
  "tempo": 76,
  "valence": 0.66,
  "energy": 0.28,
  "filepath": "audio/public/please-calm-my-mind.mp3",
  "scene_image": "https://...",
  "scene_theme": "soft piano, quiet room, slow breathing",
  "license": "Pixabay Content License",
  "source_url": "https://pixabay.com/music/beautiful-plays-please-calm-my-mind-125566/",
  "attribution": "Music by music_for_video on Pixabay"
}
```

## Scene Image Replacement

The app currently uses stable placeholder URLs from Picsum. That is fine for layout testing, but the public portfolio version should use images from Pexels or Pixabay with recorded source data.

### Pexels API

Pexels is the recommended first choice. Pexels API requires an API key in the `Authorization` header. The default free limits are 200 requests per hour and 20,000 requests per month. Their docs ask API users to show a prominent Pexels link and credit photographers when possible.

Docs:

https://www.pexels.com/api/documentation/

Run:

```bash
$env:PEXELS_API_KEY="your-key"
python scripts/fetch_scene_images.py pexels
```

### Pixabay API

Pixabay API also requires an API key. The API returns image URLs plus page URLs and user names. The docs request that users show where images/videos are from when search results are displayed.

Docs:

https://pixabay.com/api/docs/

Run:

```bash
$env:PIXABAY_API_KEY="your-key"
python scripts/fetch_scene_images.py pixabay
```

## Good Scene Queries

Use queries that describe a mood, not just a genre:

- `sunlit window green leaves calm piano`
- `rainy window reflective lofi`
- `quiet bedroom warm lamp recovery music`
- `morning forest path acoustic chill`
- `ocean horizon ambient focus`
- `rainy city lights lofi lounge`
- `coffee shop window lofi study`
- `soft garden sunlight happy acoustic`

## Final Public Release Checklist

- Every public MP3 has a `source_url`.
- Every public MP3 has a `license`.
- Every public MP3 has an `attribution`.
- Every public image has a `scene_source_url`.
- Every public image has a `scene_license`.
- README mentions that media comes from public-safe sources.
- Demo no longer depends only on fallback audio.
