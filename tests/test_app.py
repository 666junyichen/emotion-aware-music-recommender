from app import app


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


def test_stop_resets_session():
    client = app.test_client()
    client.post("/simulate", data={"bpm": "76"})

    response = client.post("/stop")

    assert response.status_code == 200
    assert b"Music stopped" in response.data
