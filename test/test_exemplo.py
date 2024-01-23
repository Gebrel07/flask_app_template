from flask import Flask


def test_hello(app: Flask):
    with app.test_client() as client:
        resp = client.get("/")
    assert "Hello from Flask" in resp.text


def test_erro(app: Flask):
    with app.test_client() as client:
        resp = client.get("/erro")
    assert "Internal Server Error" in resp.text
