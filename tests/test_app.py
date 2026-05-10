from app import app


def test_home_page_loads():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Zen Music Recommender" in response.data


def test_simulate_redirects_to_result():
    client = app.test_client()

    response = client.post("/simulate", data={"bpm": "76"}, follow_redirects=True)

    assert response.status_code == 200
    assert b"BPM 76" in response.data
    assert b"low emotional state" in response.data
    assert b"Public demo audio is playing" in response.data
    assert b"demo-sad.wav" in response.data


def test_stop_resets_session():
    client = app.test_client()
    client.post("/simulate", data={"bpm": "76"})

    response = client.post("/stop")

    assert response.status_code == 200
    assert b"Music stopped" in response.data
