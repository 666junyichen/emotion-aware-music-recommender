# PulseScape

PulseScape is a heartbeat-based music recommendation sanctuary. It maps a user's current heart-rate BPM to an emotional listening state, recommends a matching track, explains the ranking logic, and presents the music inside an immersive scene-based player.

The project began as **Zen Music Recommender**, an emotion-aware Flask prototype using ECG/HRV-inspired modelling and a curated music metadata library. It has now been redesigned into a portfolio-ready web demo with playable public audio, visual scene images, feedback collection, and Vercel deployment support.

Production site:

```text
https://emotion-aware-music-recommender.vercel.app
```

## Current Features

- Heart-rate BPM input with validation.
- BPM-to-emotion mapping using exported predictions plus a rule-based fallback.
- Transparent recommendation scoring using emotion, tempo, energy, and valence.
- Immersive recommendation room with track-specific scene images.
- "Why this track" explanation.
- Similar-track recommendations.
- Clickable library and similar-track cards that open the selected track in the player.
- Music library page with richer metadata.
- Browser `localStorage` favorites.
- `Like`, `Not for me`, and after-listening BPM feedback.
- Optional MongoDB Atlas persistence for feedback events.
- 10 public MP3 tracks under `static/audio/public/` with license/source/attribution metadata.
- Downloaded Pixabay scene images under `static/images/scenes/`.
- Public-safe demo audio fallback when licensed track files are not included.
- Vercel configuration for deployment.

## Architecture

- Backend: Flask routes in `app.py`.
- Database helper: optional MongoDB feedback persistence in `database.py`.
- Frontend: Jinja template in `templates/index.html`.
- Styling: `static/css/style.css`.
- Music data: `music.json`.
- BPM emotion predictions: `predictions.json`.
- Scene image fetcher: `scripts/fetch_scene_images.py`.
- Modelling evidence: `emotion_model.ipynb`.
- Design brief: `DESIGN.md`.
- Chinese roadmap: `docs/项目现状与下一步.md`.
- Public media sourcing notes: `docs/public-media-sourcing.md`.
- Scene image API setup: `docs/scene-image-api-setup.md`.
- MongoDB notes: `docs/mongodb-expansion-plan.md`.

## Recommendation Logic

The recommender ranks tracks with a lightweight scoring model:

```text
score =
  emotion_match * 40
+ bpm_closeness * 30
+ energy_match * 15
+ valence_match * 10
+ feedback_adjustment
+ small_random_variation
```

This keeps the demo explainable while still making recommendations feel more intentional than random selection.

## Scene Images

The project can use either Pexels or Pixabay for track scene images.

Pexels is still the preferred API for emotional scene search, but the current Pexels key returned `403 Forbidden` during testing. If that happens, verify the Pexels account email, application status, terms acceptance, or regenerate the key.

Pixabay was tested successfully and used to download local scene images into:

```text
static/images/scenes/
```

The script writes these fields back into `music.json`:

- `scene_image`
- `scene_source_url`
- `scene_attribution`
- `scene_license`
- `scene_query`

Run the image fetcher:

```powershell
$env:PEXELS_API_KEY="your-key"
python scripts/fetch_scene_images.py pexels

$env:PIXABAY_API_KEY="your-key"
python scripts/fetch_scene_images.py pixabay
```

Do not commit API key files or `.env` files.

## MongoDB

MongoDB is optional. The app still works without a database.

When configured, `/feedback` writes feedback events to MongoDB:

```text
database: pulsescape
collection: feedback
```

Local setup:

```text
MONGODB_URI=mongodb+srv://...
MONGODB_DB=pulsescape
```

The existing free `owlswap-cluster` can be reused. A separate paid cluster is not required; use a separate database name such as `pulsescape` to keep this project's data isolated.

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Run tests:

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## Deploy to Vercel

This repo includes `vercel.json` for a Flask deployment through Vercel's Python runtime.

Set environment variables in Vercel Project Settings:

```text
MONGODB_URI
MONGODB_DB=pulsescape
FLASK_SECRET_KEY
```

Deploy:

```bash
npx vercel link
npx vercel deploy --prod --yes
```

## Secret Safety

API keys, MongoDB passwords, Cloudinary credentials, and `.env` files should not be committed.

If a key has been shared in chat, screenshots, or a committed file, rotate it in the provider dashboard and update the local/Vercel environment variables.

## 中文说明

PulseScape 是一个根据用户当前心率 BPM 推荐音乐的 Web Demo。用户输入 BPM 后，系统会推断当前情绪状态，并根据歌曲 BPM、情绪、energy、valence、用户反馈等字段推荐歌曲。

目前已经完成：

- 心率输入和情绪映射。
- 可解释的音乐推荐评分。
- 沉浸式音乐播放器。
- 相似音乐推荐。
- 音乐库和相似音乐卡片点击播放。
- 10 首可播放的公开 MP3。
- Pixabay 场景图下载和本地静态资源接入。
- Like / Not for me / 听后 BPM 反馈。
- MongoDB Atlas 可选反馈持久化。
- Vercel 部署配置。

更详细的中文项目说明和下一步计划见 [docs/项目现状与下一步.md](docs/项目现状与下一步.md)。
