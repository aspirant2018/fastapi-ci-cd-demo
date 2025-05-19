from fastapi.testclient import TestClient
from main import app
import logging

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_square_number():
    response = client.get("/square/4")

    assert response.status_code == 200
    assert response.json() == {"number": 4, "square": 16}
