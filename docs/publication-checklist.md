# Publication Checklist

Use this checklist before pushing the repository to a public GitHub profile.

## Safe To Publish

- `README.md`
- `项目说明.md`
- `docs/README.md`
- `docs/project-summary.md`
- `docs/contribution-summary.md`
- `docs/metrics-and-methods.md`
- `docs/publication-checklist.md`
- `app.py`, after checking comments and secret values.
- `music.json`, if the referenced music assets are allowed to be shared.
- `predictions.json`, because it contains only BPM-to-emotion mappings.
- `installation_guide.md`, after text cleanup if desired.

## Review Before Publishing

- `emotion_model.ipynb`: check that local absolute paths have been replaced with generic relative paths before public release.
- The final report PDF currently in the root directory should not be published unless it is renamed, redacted, and checked for private or project-origin-identifying information.
- `templates.zip`: should be extracted or replaced with normal source files if the full web UI is intended to be runnable from GitHub.
- Audio, album, image, and icon assets: publish only if licensing allows public sharing.
- External ECG dataset files: do not commit unless the dataset license explicitly allows redistribution.

## Do Not Include In Public Documentation

- Institutional identifiers.
- Private account identifiers.
- Personal names or profile details.
- Local absolute paths that reveal a user name.
- Private email addresses.
- Claims that the prototype is a clinical or production-grade emotion detection system.

## Recommended Repository Name

`emotion-aware-music-recommender`

This name is clearer than a general multimedia retrieval title because it communicates the project domain, method, and output in one phrase.
