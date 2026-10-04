from server import create_app

app = create_app()


def test_index_route():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
