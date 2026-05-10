# Project Summary

## Zen Music Recommender

Zen Music Recommender is a prototype for emotion-aware music recommendation. It accepts a heart-rate BPM input, maps the input to an emotional state, and recommends music from a curated metadata library.

## Problem

Music recommendation systems usually rely on listening history, genre, or manual preference input. This prototype explores a different signal: using physiological indicators to infer an emotional state and produce a music recommendation that reflects the user's current rhythm.

## Solution

The prototype combines three parts:

- An ECG feature extraction and emotion modelling workflow.
- A structured music library labelled by emotional category.
- A Flask web application that connects BPM input, emotion mapping, recommendation, playback, and feedback.

## Public Results

- 15 curated music records.
- 3 emotion labels: `Happy`, `Sad`, and `Calm`.
- 5 tracks per emotion label.
- 50 exported BPM-to-emotion prediction mappings.
- Recorded Random Forest notebook accuracy: 83.33%.

## Tech Stack

- Python
- Flask
- NeuroKit2
- pandas
- scikit-learn
- JSON
- HTML and JavaScript

## Runnable Demo

The repository includes a minimal public Flask template so the web prototype can run without private media assets. The richer media experience can be restored by adding licensed static audio, album, image, and icon assets under `static/`.
