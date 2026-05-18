# PulseScape Design Brief

## Product Name

PulseScape: Heartbeat-Based Music Sanctuary

## One-Line Concept

PulseScape is an emotion-aware music web experience that turns a user's current heart-rate BPM into a calming, immersive music room with personalized song recommendations, scenic visuals, favorites, and similar-track discovery.

## Product Goal

The current prototype already proves the core idea: users enter a heart-rate BPM, the system maps it to an emotional state, and the app recommends music. The next design should make the demo feel less like a simple form and more like a polished emotional music product.

The new web experience should combine two directions:

- A healing, immersive music sanctuary with soft scenic backgrounds and responsive playback visuals.
- A lightweight recommendation system that explains why a track was selected and helps users discover similar music.

## Target User

The target user is someone who wants music that matches or gently regulates their emotional state. They may be studying, resting, journaling, recovering from stress, or looking for calm background music.

The product should feel quiet, sensory, and trustworthy rather than loud or overly clinical.

## Core User Flow

1. The user lands on a calm full-screen page.
2. They enter their current heart-rate BPM.
3. The system maps the BPM to an emotional state such as Calm, Sad, Happy, Focused, Restless, or Recovery.
4. The app recommends a track that best matches the user's heart rate, mood, tempo, energy, and valence.
5. The recommendation page becomes a scenic music room with a track-specific background image.
6. The user can play or pause the track, favorite it, skip to another recommendation, or open similar songs.
7. After listening, the user can confirm whether the recommendation matched their mood.
8. The app uses liked tracks and feedback to improve similar-track recommendations.

## Visual Direction

The design should feel like a soft emotional landscape rather than a standard music app.

Use track-specific scenic backgrounds such as:

- Sunlit window with green leaves for bright calm music.
- Rain on lotus leaves for reflective or melancholic music.
- Warm bedroom at night for recovery music.
- Morning forest path for hopeful acoustic music.
- Slow ocean horizon for ambient focus music.
- City lights through rain for gentle vocal music.

The UI should use translucent overlays, restrained typography, slow breathing animation, and enough contrast for readability. Avoid a generic gradient-only background. The main visual signal should be the music scene itself.

### Mood Examples

Calm:

- Soft green, pale yellow, mist blue.
- Slow breathing motion.
- Window, trees, water, morning light.

Sad / Reflective:

- Rain, glass, deep green, muted blue.
- Slow waveform.
- Quiet lyric or piano atmosphere.

Happy / Uplifted:

- Warm sunlight, citrus, open sky.
- Slightly quicker pulse animation.
- Brighter player controls.

Focused:

- Dark neutral room, desk lamp, low contrast.
- Minimal movement.
- Ambient or instrumental music.

Recovery:

- Warm dusk, bedroom, slow glow.
- Very soft transitions.
- Low energy tracks.

## Page Structure

### 1. Landing Page

Purpose: capture the user's current heart-rate BPM and set the emotional tone.

Required elements:

- Product name: PulseScape.
- Short subtitle: "Find music that moves with your heartbeat."
- BPM input field.
- Primary action button: "Find my track".
- Small sample chips: 62, 76, 88, 104, 122.
- Ambient pulse visual that gently expands and contracts.
- Optional note: "This is a music recommendation demo, not medical advice."

Layout:

- Full viewport.
- Background can be a soft, real scenic image or generated atmospheric scene.
- Center the BPM input and primary action.
- Keep the first screen focused. Do not make it a marketing landing page.

### 2. Recommendation Room

Purpose: show the selected song as an immersive emotional scene.

Required elements:

- Full-screen track-specific background image.
- Large track title.
- Artist name.
- Emotion label.
- BPM chip: user BPM and track BPM.
- Audio player controls.
- Favorite button.
- Skip / recommend another button.
- "Why this track" explanation.
- Similar tracks section.

Layout:

- Background image fills the screen.
- A readable player panel sits over the image but should not feel like a heavy card.
- Use a glassy or translucent overlay only where text needs contrast.
- The player should visually respond to playback with a waveform, ring, or pulse animation.

### 3. Why This Track

Purpose: make the recommendation system understandable.

Example copy:

"Your BPM is 82, close to this track's 80 BPM. Its low energy and warm valence match a calm recovery state."

Inputs used:

- User BPM.
- Predicted emotion.
- Track tempo.
- Track energy.
- Track valence.
- Genre.
- Vocal type.
- Favorite history, if available.

### 4. Similar Tracks

Purpose: make the demo feel like a real recommendation product.

Display 3 to 5 similar songs based on:

- Close tempo.
- Same or adjacent emotion.
- Similar energy.
- Similar valence.
- Same genre or vocal type.
- User liked/favorited songs.

Each similar track item should include:

- Small cover or scene thumbnail.
- Track title.
- Artist.
- BPM.
- Mood tag.
- Genre tag.

### 5. Music Library

Purpose: show the expanded dataset and make the project feel richer.

Filters:

- Mood.
- Genre.
- Vocal / instrumental.
- Tempo range.
- Energy level.

Suggested genres:

- Ambient.
- Piano.
- Lofi.
- Acoustic.
- Soft pop.
- Jazz.
- Cinematic.
- Electronic chill.
- Gentle vocal.
- Nature soundscape.

## Data Model

Upgrade each music record in `music.json` to support visual scenes, recommendation scoring, licensing, and future deployment.

Example:

```json
{
  "id": "magnolia-window",
  "title": "Magnolia",
  "artist": "Example Artist",
  "emotion": "Calm",
  "genre": "ambient piano",
  "vocal_type": "instrumental",
  "tempo": 78,
  "valence": 0.68,
  "energy": 0.28,
  "filepath": "audio/magnolia.mp3",
  "cover": "album/magnolia.jpg",
  "scene_image": "images/scenes/magnolia-window.jpg",
  "scene_theme": "sunlit window, green leaves, soft morning air",
  "scene_prompt": "A dreamy sunlit magnolia tree seen through an open window, soft green leaves, gentle morning light, calming music cover art, cinematic but peaceful",
  "license": "Pixabay Content License",
  "source_url": "https://pixabay.com/music/",
  "attribution": "Music by Example Artist"
}
```

## Recommendation Logic

The current prototype selects a random track from the predicted emotion. The next version should use a transparent scoring system.

Suggested scoring:

```text
score =
  emotion_match * 40
+ bpm_closeness * 30
+ energy_match * 15
+ valence_match * 10
+ favorite_similarity * 5
```

Where:

- `emotion_match` is 1 if track emotion matches predicted emotion, 0.5 for adjacent emotion, and 0 otherwise.
- `bpm_closeness` is higher when the track tempo is close to user BPM.
- `energy_match` compares track energy with the expected energy for the emotional state.
- `valence_match` compares track valence with the expected mood.
- `favorite_similarity` increases if the track is similar to songs the user previously liked.

Example BPM-to-emotion mapping:

```text
40-64 BPM: Sad / Recovery
65-84 BPM: Calm
85-100 BPM: Focused / Balanced
101-125 BPM: Happy / Energized
126+ BPM: Restless / High Energy
```

This mapping can still use the existing exported prediction JSON first, then use the rule-based mapping as fallback.

## Favorites and Feedback

The user should be able to:

- Favorite a song.
- Remove a favorite.
- See favorite songs in a small library panel.
- Answer whether the recommendation matched their feeling.
- Ask for similar music based on the current or favorited track.

For a simple deployed demo, favorites can be stored in browser `localStorage`. A later version can use a database.

## Free Music Sources

Recommended sources for adding public-safe music:

- Pixabay Music: good for free demo tracks. Record the source URL and license for every track.
- Free Music Archive: useful for Creative Commons tracks, but check each individual license.
- ccMixter: useful for Creative Commons vocal and remix-friendly tracks.
- Musopen: useful for classical, piano, and public-domain style recordings.

Do not add copyrighted songs from Spotify, Apple Music, YouTube, or commercial albums unless the project has explicit redistribution rights.

Every added track should include:

- Source URL.
- License.
- Attribution.
- Whether commercial use is allowed.
- Whether modification is allowed.
- Download date.

## Stitch / Web Generator Prompt

Use this prompt in Stitch or another web generator:

```text
Create a polished responsive web app called "PulseScape", a heartbeat-based music recommendation sanctuary.

The app should combine a calming immersive music experience with a lightweight recommendation-system UI.

Core experience:
- The first screen asks the user to enter their current heart-rate BPM.
- The UI should feel quiet, therapeutic, musical, and atmospheric, not medical or corporate.
- After the user submits BPM, show a recommendation room with a full-screen scenic background image matched to the recommended song.
- The recommended song should display title, artist, mood, genre, user BPM, track BPM, energy, and valence.
- Include a beautiful custom music player with play/pause, favorite, skip, and "similar tracks" actions.
- Add a "Why this track" section explaining the recommendation in one short sentence.
- Show 3 to 5 similar tracks as compact items with cover thumbnails, BPM, mood, and genre tags.
- Include a music library view with filters for mood, genre, vocal/instrumental, and tempo range.

Visual style:
- Use full-bleed scenic imagery such as sunlit windows, rainy lotus leaves, forest mornings, quiet bedrooms, ocean horizons, and rainy city lights.
- Each track should feel like its own emotional scene.
- Use soft translucent overlays for readable text.
- Use slow breathing animations, pulse rings, and gentle waveform movement.
- Keep typography elegant and readable.
- Avoid generic gradient-only backgrounds.
- Avoid a marketing landing page. Build the actual app as the first screen.

Pages or states:
1. BPM input state.
2. Recommendation room state.
3. Similar tracks area.
4. Music library area.
5. Favorites panel.

Data fields for each track:
- id
- title
- artist
- emotion
- genre
- vocal_type
- tempo
- valence
- energy
- filepath
- cover_image
- scene_image
- scene_theme
- license
- source_url
- attribution

Recommendation behavior:
- Map BPM to an emotional state.
- Rank songs by emotion match, BPM closeness, energy match, valence match, and favorite similarity.
- Explain the selected recommendation in plain language.
- Allow favorites to be stored locally.

Tone:
- The app should feel like stepping into a quiet music room generated from your heartbeat.
- It should look sophisticated enough for a portfolio project and clear enough for users to understand immediately.
```

## Implementation Notes for This Repository

Current project stack:

- Flask backend in `app.py`.
- Jinja template in `templates/index.html`.
- CSS in `static/css/style.css`.
- Music metadata in `music.json`.
- Demo audio in `static/audio`.

Recommended next implementation steps:

1. Extend `music.json` with `id`, `genre`, `vocal_type`, `scene_image`, `scene_theme`, `license`, `source_url`, and `attribution`.
2. Replace random recommendation with scoring-based recommendation.
3. Add similar-track calculation.
4. Add favorites using browser `localStorage`.
5. Update the template into separate UI sections: landing, recommendation room, similar tracks, and library.
6. Add real public-safe music and scene images gradually.
7. Deploy to Vercel only after audio/image licensing is checked.

## Success Criteria

The redesign is successful if:

- A new visitor understands the product within 5 seconds.
- The page feels emotional and music-centered, not like a simple form demo.
- Each recommended song has its own visual identity.
- The recommendation includes a clear explanation.
- The user can favorite a song and discover similar tracks.
- The project looks strong enough for a GitHub README, portfolio, and Vercel demo.
