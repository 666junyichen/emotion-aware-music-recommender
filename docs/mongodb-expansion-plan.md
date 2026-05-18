# MongoDB Expansion Plan

## Current Status

MongoDB feedback persistence has been added as an optional enhancement.

The app still works without MongoDB. When `MONGODB_URI` is present, feedback events from `/feedback` are written to the `feedback` collection in the configured database.

Verified local connection:

```text
MONGODB_DB=pulsescape
Atlas ping result: ok
```

## Can This Project Use MongoDB?

Yes. MongoDB Atlas is a good next step if PulseScape needs cross-device favorites, persistent feedback, and user-specific recommendation history.

The current app stores favorites in browser `localStorage` and feedback in the Flask session. This is enough for a portfolio demo, but it does not follow the user across devices.

## Recommended MongoDB Collections

### `users`

```json
{
  "_id": "user_id",
  "display_name": "Guest user",
  "created_at": "2026-05-18T00:00:00Z"
}
```

### `favorites`

```json
{
  "_id": "favorite_id",
  "user_id": "user_id",
  "track_id": "public-chopin-nocturne-op-9-no-2",
  "created_at": "2026-05-18T00:00:00Z"
}
```

### `feedback`

```json
{
  "_id": "feedback_id",
  "user_id": "user_id",
  "track_id": "public-chopin-nocturne-op-9-no-2",
  "action": "like",
  "pre_bpm": 76,
  "post_bpm": 70,
  "created_at": "2026-05-18T00:00:00Z"
}
```

### `recommendation_events`

```json
{
  "_id": "event_id",
  "user_id": "user_id",
  "input_bpm": 76,
  "predicted_emotion": "Calm",
  "recommended_track_id": "public-chopin-nocturne-op-9-no-2",
  "score_breakdown": {
    "emotion": 40,
    "bpm": 28,
    "energy": 13,
    "valence": 9
  },
  "created_at": "2026-05-18T00:00:00Z"
}
```

## Environment Variables

Do not commit the MongoDB password.

Use the existing free Atlas cluster. Do not create another paid cluster just for this project.

Keep the URI pointed at the existing cluster, and separate this app by database name:

```text
MONGODB_URI=mongodb+srv://...
MONGODB_DB=pulsescape
```

You can also put the database name directly in the URI:

```text
mongodb+srv://username:password@cluster-host.mongodb.net/pulsescape?appName=cluster-name
```

However, keeping `MONGODB_DB=pulsescape` separate is clearer for this project.

For Vercel, add these in the Vercel dashboard:

Project Settings -> Environment Variables

## Minimal Implementation Steps

These steps are now mostly complete for feedback persistence:

1. Install dependency:

```bash
pip install pymongo
```

2. Add to `requirements.txt`:

```text
pymongo>=4.0
```

3. Create `database.py`.
4. Add helper functions:

- `save_feedback_event(user_id, track_id, action, pre_bpm, post_bpm)`

5. Add a simple guest user ID in session.
6. Future step: persist favorites.
7. Future step: use stored liked/disliked track IDs in `score_track` across sessions.

## Recommendation Impact

MongoDB makes these features possible:

- Favorites persist after browser/device change.
- "Like" increases similar recommendation score.
- "Not for me" lowers future recommendation score.
- Post-listening BPM can estimate whether the track helped the user settle.
- Recommendation events can be analyzed later for a stronger project report.
