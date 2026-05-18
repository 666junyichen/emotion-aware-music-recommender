import app as app_module


app = app_module.app


def test_home_page_loads():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"PulseScape" in response.data
    assert b"Find my track" in response.data


def test_simulate_redirects_to_result():
    client = app.test_client()

    response = client.post("/simulate", data={"bpm": "76"}, follow_redirects=True)

    assert response.status_code == 200
    assert b"BPM" in response.data
    assert b"Why this track" in response.data
    assert b"Similar tracks" in response.data
    assert b"Public demo audio is playing" in response.data


def test_library_page_loads():
    client = app.test_client()

    response = client.get("/library")

    assert response.status_code == 200
    assert b"Music library" in response.data
    assert b"Expanded dataset" in response.data


def test_library_track_card_opens_player():
    client = app.test_client()

    response = client.get("/track/tear-away", follow_redirects=True)

    assert response.status_code == 200
    assert b"Why this track" in response.data
    assert b"Similar tracks" in response.data
    assert b"Adi Goldstein - Tear Away" in response.data


def test_feedback_like_is_stored_in_session():
    client = app.test_client()
    client.get("/track/tear-away?bpm=76")

    response = client.post(
        "/feedback",
        data={"track_id": "tear-away", "action": "like", "post_bpm": "70"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    with client.session_transaction() as session:
        assert "tear-away" in session["feedback"]["liked"]
        assert session["feedback"]["post_listen_bpm"]["tear-away"] == 70


def test_feedback_is_persisted_when_database_is_configured(monkeypatch):
    class FakeFeedbackStore:
        def __init__(self):
            self.saved = []

        def save_feedback_event(self, **event):
            self.saved.append(event)

    fake_store = FakeFeedbackStore()
    monkeypatch.setattr(app_module, "feedback_store", fake_store)
    client = app.test_client()
    client.get("/track/tear-away?bpm=76")

    response = client.post(
        "/feedback",
        data={"track_id": "tear-away", "action": "like", "post_bpm": "70"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert fake_store.saved == [
        {
            "user_id": fake_store.saved[0]["user_id"],
            "track_id": "tear-away",
            "action": "like",
            "pre_bpm": 76,
            "post_bpm": 70,
        }
    ]
    assert fake_store.saved[0]["user_id"]


def test_stop_resets_session():
    client = app.test_client()
    client.post("/simulate", data={"bpm": "76"})

    response = client.post("/stop")

    assert response.status_code == 200
    assert b"Music stopped" in response.data
