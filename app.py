from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
import random

from dotenv import load_dotenv

from database import create_feedback_store, new_guest_user_id

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")
feedback_store = create_feedback_store()


def load_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


music_library = load_json("music.json")
predicted_emotions = load_json("predictions.json")


emotion_profiles = {
    "Sad": {
        "target_energy": 0.35,
        "target_valence": 0.25,
        "adjacent": ["Recovery", "Calm"],
        "message": (
            "Your heart rhythm suggests a quiet, reflective state.\n"
            "This track keeps the energy low and gives the feeling room to soften."
        ),
    },
    "Calm": {
        "target_energy": 0.32,
        "target_valence": 0.68,
        "adjacent": ["Recovery", "Focused", "Sad"],
        "message": (
            "Your heartbeat feels steady and centered.\n"
            "This recommendation follows that rhythm with a gentle, spacious sound."
        ),
    },
    "Focused": {
        "target_energy": 0.5,
        "target_valence": 0.58,
        "adjacent": ["Calm", "Happy"],
        "message": (
            "Your BPM sits in a balanced range.\n"
            "This track keeps enough motion for focus without becoming too bright."
        ),
    },
    "Happy": {
        "target_energy": 0.78,
        "target_valence": 0.88,
        "adjacent": ["Focused", "Calm"],
        "message": (
            "A lively heartbeat came through.\n"
            "This track leans into that lift with brighter tempo and higher energy."
        ),
    },
    "Recovery": {
        "target_energy": 0.25,
        "target_valence": 0.5,
        "adjacent": ["Sad", "Calm"],
        "message": (
            "Your BPM suggests a low-energy recovery moment.\n"
            "This track keeps the sound warm, slow, and easy to settle into."
        ),
    },
}


def map_bpm_to_emotion(bpm):
    if bpm < 65:
        return "Recovery"
    if bpm <= 84:
        return "Calm"
    if bpm <= 100:
        return "Focused"
    if bpm <= 125:
        return "Happy"
    return "Happy"


def normalized_bpm_score(user_bpm, track_tempo):
    distance = abs(user_bpm - track_tempo)
    return max(0, 1 - (distance / 70))


def emotion_score(predicted_emotion, track_emotion):
    if predicted_emotion == track_emotion:
        return 1
    adjacent = emotion_profiles.get(predicted_emotion, {}).get("adjacent", [])
    if track_emotion in adjacent:
        return 0.5
    return 0


def score_track(track, bpm, predicted_emotion):
    profile = emotion_profiles.get(predicted_emotion, emotion_profiles["Calm"])
    track_energy = float(track.get("energy", 0.5))
    track_valence = float(track.get("valence", 0.5))
    track_tempo = int(track.get("tempo", bpm))
    feedback = session.get("feedback", {})
    track_id = track.get("id", "")
    feedback_adjustment = 0

    if track_id in feedback.get("liked", []):
        feedback_adjustment += 8
    if track_id in feedback.get("disliked", []):
        feedback_adjustment -= 20

    return (
        emotion_score(predicted_emotion, track.get("emotion", "Calm")) * 40
        + normalized_bpm_score(bpm, track_tempo) * 30
        + (1 - abs(track_energy - profile["target_energy"])) * 15
        + (1 - abs(track_valence - profile["target_valence"])) * 10
        + feedback_adjustment
        + random.random() * 2
    )


def recommend_track(bpm, predicted_emotion):
    ranked = sorted(
        music_library,
        key=lambda track: score_track(track, bpm, predicted_emotion),
        reverse=True,
    )
    return ranked[0], ranked[1:5]


def find_track(track_id):
    for track in music_library:
        prepared = prepare_track(track)
        if prepared["id"] == track_id:
            return prepared
    return None


def scene_image_url(scene_image):
    if not scene_image:
        return "https://picsum.photos/seed/pulsescape-scene/1600/1000"
    if scene_image.startswith(("http://", "https://", "/static/")):
        return scene_image
    return url_for("static", filename=scene_image)


def similar_tracks_for(track, bpm):
    emotion = track.get("emotion", map_bpm_to_emotion(bpm))
    ranked = sorted(
        [prepare_track(item) for item in music_library if prepare_track(item)["id"] != track["id"]],
        key=lambda item: score_track(item, bpm, emotion),
        reverse=True,
    )
    return ranked[:4]


def build_player_payload(track, bpm, emotion):
    similar_tracks = similar_tracks_for(track, bpm)
    audio_path, track_available, audio_type = audio_for_track(track, emotion)
    return {
        "bpm": bpm,
        "emotion": emotion,
        "emotion_text": emotion_profiles[emotion]["message"],
        "reason": build_reason(track, bpm, emotion),
        "track": track,
        "similar_tracks": similar_tracks,
        "audio_path": audio_path,
        "audio_type": audio_type,
        "track_available": track_available,
        "uses_demo_audio": not track_available,
        "feedback": session.get("feedback", {}),
    }


def build_reason(track, bpm, predicted_emotion):
    tempo = int(track.get("tempo", bpm))
    energy = float(track.get("energy", 0.5))
    valence = float(track.get("valence", 0.5))
    distance = abs(bpm - tempo)

    if distance <= 5:
        tempo_phrase = f"very close to this track's {tempo} BPM"
    elif distance <= 15:
        tempo_phrase = f"near this track's {tempo} BPM"
    else:
        tempo_phrase = f"balanced against this track's {tempo} BPM"

    return (
        f"Your BPM is {bpm}, {tempo_phrase}. "
        f"Its {energy:.2f} energy and {valence:.2f} valence fit a {predicted_emotion.lower()} listening state."
    )


def audio_for_track(track, emotion):
    track_path = track.get("filepath", "")
    track_available = bool(track_path) and os.path.exists(os.path.join(app.static_folder, track_path))
    audio_type = "audio/mpeg" if track_path.lower().endswith(".mp3") and track_available else "audio/wav"
    fallback = {
        "Happy": "audio/demo-happy.wav",
        "Sad": "audio/demo-sad.wav",
        "Calm": "audio/demo-calm.wav",
        "Focused": "audio/demo-calm.wav",
        "Recovery": "audio/demo-sad.wav",
    }
    return (
        track_path if track_available else fallback.get(emotion, "audio/demo-calm.wav"),
        track_available,
        audio_type if track_available else "audio/wav",
    )


def prepare_track(track):
    prepared = dict(track)
    prepared.setdefault("id", prepared["title"].lower().replace(" ", "-"))
    prepared.setdefault("genre", "ambient")
    prepared.setdefault("vocal_type", "instrumental")
    prepared.setdefault("scene_theme", "soft atmospheric music room")
    prepared.setdefault("scene_image", f"https://picsum.photos/seed/{prepared['id']}/1600/1000")
    prepared["scene_image_url"] = scene_image_url(prepared["scene_image"])
    return prepared


@app.route("/")
def index():
    return render_template(
        "index.html",
        mode="landing",
        library=[prepare_track(track) for track in music_library[:8]],
        landing_scene_image=scene_image_url("images/scenes/public-calm-piano-background-pixabay.jpg"),
    )


@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        bpm = int(request.form["bpm"])
    except (ValueError, TypeError):
        bpm = 76

    bpm = max(40, min(180, bpm))
    predicted_emotion = predicted_emotions.get(str(bpm), map_bpm_to_emotion(bpm))
    if predicted_emotion not in emotion_profiles:
        predicted_emotion = map_bpm_to_emotion(bpm)

    track, similar_tracks = recommend_track(bpm, predicted_emotion)
    track = prepare_track(track)
    similar_tracks = [prepare_track(item) for item in similar_tracks]

    payload = build_player_payload(track, bpm, predicted_emotion)
    payload["similar_tracks"] = similar_tracks
    session["track"] = payload

    return redirect(url_for("result"))


@app.route("/result")
def result():
    payload = session.get("track")
    if not payload:
        return redirect(url_for("index"))

    return render_template("index.html", mode="result", library=music_library, **payload)


@app.route("/track/<track_id>")
def play_track(track_id):
    track = find_track(track_id)
    if not track:
        return redirect(url_for("library"))

    try:
        bpm = int(request.args.get("bpm", track.get("tempo", 76)))
    except (ValueError, TypeError):
        bpm = int(track.get("tempo", 76))

    bpm = max(40, min(180, bpm))
    emotion = track.get("emotion", map_bpm_to_emotion(bpm))
    if emotion not in emotion_profiles:
        emotion = map_bpm_to_emotion(bpm)

    session["track"] = build_player_payload(track, bpm, emotion)
    return redirect(url_for("result"))


@app.route("/feedback", methods=["POST"])
def feedback():
    track_id = request.form.get("track_id", "")
    action = request.form.get("action", "")
    post_bpm = request.form.get("post_bpm", "").strip()
    current = session.get("feedback", {"liked": [], "disliked": [], "post_listen_bpm": {}})
    parsed_post_bpm = None

    current.setdefault("liked", [])
    current.setdefault("disliked", [])
    current.setdefault("post_listen_bpm", {})

    if action == "like" and track_id:
        if track_id not in current["liked"]:
            current["liked"].append(track_id)
        if track_id in current["disliked"]:
            current["disliked"].remove(track_id)
    elif action == "dislike" and track_id:
        if track_id not in current["disliked"]:
            current["disliked"].append(track_id)
        if track_id in current["liked"]:
            current["liked"].remove(track_id)

    if post_bpm and track_id:
        try:
            parsed_post_bpm = max(40, min(180, int(post_bpm)))
            current["post_listen_bpm"][track_id] = parsed_post_bpm
        except ValueError:
            pass

    session["feedback"] = current
    if track_id and (action in {"like", "dislike"} or parsed_post_bpm is not None):
        session.setdefault("user_id", new_guest_user_id())
        feedback_store.save_feedback_event(
            user_id=session["user_id"],
            track_id=track_id,
            action=action or "post_bpm",
            pre_bpm=session.get("track", {}).get("bpm"),
            post_bpm=parsed_post_bpm,
        )

    if "track" in session:
        session["track"]["feedback"] = current
    return redirect(url_for("result"))


@app.route("/library")
def library():
    return render_template("index.html", mode="library", library=[prepare_track(track) for track in music_library])


@app.route("/stop", methods=["POST"])
def stop():
    session.clear()
    return render_template(
        "index.html",
        mode="landing",
        library=[prepare_track(track) for track in music_library[:8]],
        landing_scene_image=scene_image_url("images/scenes/public-calm-piano-background-pixabay.jpg"),
        emotion_text="Music stopped. You can try another heartbeat.",
    )


if __name__ == "__main__":
    app.run(debug=True)
