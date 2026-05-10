# Metrics and Methods

## Metrics Verified From Repository Files

| Metric | Value | Source |
| --- | ---: | --- |
| Music records | 15 | `music.json` |
| Emotion classes in music library | 3 | `music.json` |
| Tracks per emotion class | 5 | `music.json` |
| Exported BPM prediction mappings | 50 | `predictions.json` |
| BPM range in exported mapping | 52 to 131 | `predictions.json` |
| Recorded notebook accuracy | 83.33% | `emotion_model.ipynb` output |

## Music Metadata

Each music record contains:

- `title`
- `artist`
- `emotion`
- `valence`
- `energy`
- `tempo`
- `filepath`
- `cover`

The public music library covers `Happy`, `Sad`, and `Calm` recommendation categories.

## Modelling Workflow

The notebook workflow uses ECG signal processing to extract physiological features for emotion classification.

Feature set:

- `RMSSD`
- `SDNN`
- `LF_HF`
- `BPM`

Processing and modelling tools:

- NeuroKit2 for ECG and HRV feature extraction.
- pandas for tabular feature assembly.
- StandardScaler for feature scaling.
- LabelEncoder for emotion label encoding.
- RandomForestClassifier with 100 estimators for classification.

## Recommendation Workflow

1. User submits BPM in the web interface.
2. The Flask route checks `predictions.json` for a model-exported emotion mapping.
3. If the BPM is not found in the prediction file, the application uses a rule-based fallback:
   - BPM below 65 maps to `Sad`.
   - BPM above 100 maps to `Happy`.
   - BPM between those ranges maps to `Calm`.
4. The application filters `music.json` by emotion label.
5. One matching track is selected and rendered in the playback interface.

## Limitations

- The recorded accuracy comes from the notebook experiment and should be treated as prototype evidence, not production validation.
- The web prototype uses BPM as the runtime input, while the modelling workflow uses richer ECG-derived HRV features.
- The recommendation library is small and curated for demonstration purposes.
