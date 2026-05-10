# Contribution Summary

## Implementation Scope

The project work covered the data-to-interface flow for an emotion-aware music recommendation prototype.

## Key Contributions

- Built the BPM-driven recommendation flow that converts user heart-rate input into an emotional state and selects a matching track.
- Designed the music metadata schema in `music.json`, including title, artist, emotion label, valence, energy, tempo, audio path, and cover path.
- Implemented the Flask application routes for the landing page, simulation submission, recommendation result, and playback reset.
- Connected exported emotion predictions from `predictions.json` to the web recommendation flow, with a rule-based fallback for unmapped BPM values.
- Added interactive playback UI behaviour, including album display, BPM display, rhythm-synchronized animation, input validation, and feedback popup logic.
- Ran an ECG-based modelling workflow using HRV features and a Random Forest classifier.

## Resume-Ready Bullet Options

- Built an emotion-aware Flask music recommender that maps BPM input to emotional states and returns matching audio recommendations.
- Extracted ECG-derived HRV features with NeuroKit2 and trained a Random Forest classifier for emotion prediction.
- Achieved 83.33% recorded notebook accuracy using `RMSSD`, `SDNN`, `LF_HF`, and `BPM` features.
- Designed a structured 15-track music metadata library across 3 emotion categories for recommendation retrieval.
- Integrated model-exported BPM emotion mappings into a working web prototype with input validation, playback UI, and feedback collection.

## Public Positioning

This project can be described publicly as a multimedia retrieval and emotion-aware recommendation prototype. It should not be presented as a deployed commercial product or a clinical emotion detection system.
