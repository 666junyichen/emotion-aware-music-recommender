# Reproduction Guide

## What The Demo Shows

The reviewed demo recording shows a local Flask web app running in a browser at:

```text
127.0.0.1:5000
```

The demonstrated flow is:

1. Open the Zen Music Recommender home page.
2. Enter a BPM value.
3. Submit the input.
4. View the recommendation result page.
5. See the selected track, emotion text, animated visual state, and feedback popup.
6. Reset and try another BPM value.

## How To Reproduce The Public Demo

Install the runtime dependency:

```bash
pip install -r requirements.txt
```

Start the Flask app:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Try values such as:

- `76`
- `78`
- `100`
- `67`

Run the route smoke tests:

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## Current Public Version

The public repository includes a minimal runnable template and no private media assets. It reproduces the core flow: BPM input, emotion mapping, recommendation rendering, and reset.

## Full Media Demo Requirements

To reproduce the original richer visual/audio demo, the following assets would need to be added under `static/` only if redistribution is allowed:

- `static/css/style.css`
- `static/audio/`
- `static/album/`
- `static/images/`
- `static/icons/`
- `static/fonts/`

The public repository intentionally does not include the original audio, album artwork, fonts, or raw screen recording.
