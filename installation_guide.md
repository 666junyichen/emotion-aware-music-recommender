# Installation Guide

This guide explains how to run the Zen Music Recommender Flask prototype locally.

## Prerequisites

- Python 3.7 or higher
- pip
- A modern browser

## Setup

1. Clone or download the repository.
2. Open a terminal in the project root.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

5. Open the local URL shown by Flask, usually:

```text
http://127.0.0.1:5000
```

## Usage

1. Enter a heart-rate BPM value.
2. The app maps the BPM to an emotion using exported predictions or a fallback rule.
3. The app selects a matching track from `music.json`.
4. The result page displays the BPM, emotion text, track information, and playback UI.

## Notes

- The web UI expects template and static assets to be present in the expected Flask folders.
- The notebook workflow requires access to the ECG dataset and additional modelling dependencies.
- The current project is a prototype and should not be treated as a clinical or production-grade emotion detection system.

## Troubleshooting

- If Flask is missing, rerun `pip install -r requirements.txt`.
- If the port is already in use, run Flask on another port with `flask run --port=5001`.
- If audio or images do not load, check that referenced static asset paths exist locally.
