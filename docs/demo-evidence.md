# Demo Evidence

This note summarizes the reviewed demo package in a public-safe format. Original binary files such as reports, slide decks, packaged source folders, and videos are not committed because they may contain private identifiers, authorship metadata, course-specific naming, or media licensing risks.

## Reviewed Materials

The reviewed package contained:

- A Flask application prototype.
- A richer `templates/index.html` frontend.
- Static assets for CSS, icons, album artwork, fonts, and audio.
- A video demonstration.
- A project readme PDF.
- A final report PDF.
- Presentation slides.
- Music metadata and BPM-to-emotion prediction files.

## Public-Safe Evidence

The following evidence has been folded into the public repository:

- The repository now includes a runnable Flask demo with a public-safe template.
- The documented feature set includes BPM input, emotion mapping, music retrieval, playback UI logic, animation concepts, and user feedback.
- The metrics documentation records the verified project numbers: 15 music records, 3 emotion classes, 50 BPM-to-emotion mappings, and 83.33% recorded notebook accuracy.
- The method documentation records ECG feature extraction using `RMSSD`, `SDNN`, `LF_HF`, and `BPM`, plus Random Forest classification.
- The public README and project docs describe the demo without private identifiers.

## Demo Features Evidenced By The Package

- Manual BPM input for emotion inference.
- Hybrid emotion inference using exported predictions and rule-based fallback.
- Emotion-tagged local music retrieval.
- Dynamic visual feedback through gradients, album animation, and pulse animation.
- Feedback popup for evaluating emotional alignment.
- Post-Redirect-Get flow for refresh-safe interaction.

## Not Published Directly

- Original final report PDF: contains private identifiers.
- Original project readme PDF: contains contributor names and course-specific filenames.
- Original slide deck: contains authorship metadata in at least one copy.
- Original packaged source folder: includes nested `.git`, system metadata, duplicated code, and project-origin-specific naming.
- Audio files, album artwork, fonts, and video files: require explicit license and privacy review before redistribution.

## Publication Decision

The public repository should use the cleaned runnable demo and this evidence summary instead of publishing the original package wholesale. This keeps the GitHub project useful for reviewers while avoiding unnecessary exposure of private identifiers or redistribution-sensitive media.

## README Demo Preview

The README uses a muted, cropped, and compressed preview derived from the reviewed screen recording:

- `docs/assets/demo-preview.gif`
- `docs/assets/demo-preview.mp4`

The GIF plays directly in the README, and clicking it opens the MP4 version. The preview removes the browser address bar and source audio.
