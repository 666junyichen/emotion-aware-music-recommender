from flask import Flask, render_template, request, redirect, url_for, session
import json
import os
import random

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key")

# Load the curated music library.
with open("music.json", "r") as f:
    music_library = json.load(f)

with open("predictions.json", "r") as f:
    predicted_emotions = json.load(f)


# Rule-based fallback for BPM-to-emotion mapping.
def map_bpm_to_emotion(bpm):
    if bpm < 65:
        return "Sad"
    elif bpm > 100:
        return "Happy"
    else:
        return "Calm"


# Emotion messages shown on the recommendation page.
emotion_messages = {
    "Happy": (
        "A lively heartbeat detected!\n"
        "You seem to be glowing with joy and vitality.\n"
        "Let's celebrate your energy with uplifting music."
    ),
    "Sad": (
        "Your heart rhythm suggests a quiet, low emotional state.\n"
        "You're not alone - even cloudy skies pass.\n"
        "Let these gentle tunes carry you through."
    ),
    "Calm": (
        "Your heart beats with steady rhythm and clarity.\n"
        "You seem to be in a peaceful, centered state.\n"
        "Let the music flow gently with your breath."
    )
}


# Emotion-level cover images.
emotion_covers = {
    "Happy": "images/Mask group-1.png",
    "Sad": "images/Mask group-2.png",
    "Calm": "images/Mask group.png"
}

demo_audio = {
    "Happy": "audio/demo-happy.wav",
    "Sad": "audio/demo-sad.wav",
    "Calm": "audio/demo-calm.wav"
}


@app.route("/")
def index():
    return render_template("index.html", track_title=None)


@app.route("/simulate", methods=["POST"])
def simulate():
    try:
        bpm = int(request.form["bpm"])
    except ValueError:
        bpm = 76

    # Use exported predictions first, then fall back to the rule-based mapping.
    emotion = predicted_emotions.get(str(bpm), map_bpm_to_emotion(bpm))

    # Select a matching track from the emotion-labelled music library.
    matches = [track for track in music_library if track["emotion"].lower() == emotion.lower()]
    track = random.choice(matches) if matches else {"title": "", "filepath": "", "artist": ""}
    track_path = track["filepath"]
    track_available = bool(track_path) and os.path.exists(os.path.join(app.static_folder, track_path))
    audio_path = track_path if track_available else demo_audio[emotion]

    # Store recommendation data for the result page.
    session["track"] = {
        "bpm": bpm,
        "emotion": emotion,
        "emotion_text": emotion_messages[emotion],
        "track_title": track["title"],
        "track_artist": track["artist"],
        "cover_image": emotion_covers[emotion],
        "cover": track["cover"],
        "track_path": track_path,
        "audio_path": audio_path,
        "track_available": track_available,
        "uses_demo_audio": not track_available
    }

    return redirect(url_for("result"))


@app.route("/result")
def result():
    track = session.get("track")

    if not track:
        return redirect(url_for("index"))

    return render_template("index.html", **track)


@app.route("/stop", methods=["POST"])
def stop():
    session.clear()

    return render_template(
        "index.html",
        bpm=None,
        emotion="Calm",
        emotion_text="Music stopped. You can try again.",
        track_title=None,
        track_artist=None,
        cover_image=emotion_covers["Calm"],
        track_path=None,
        audio_path=None,
        track_available=False,
        uses_demo_audio=False
    )


if __name__ == "__main__":
    app.run(debug=True)
