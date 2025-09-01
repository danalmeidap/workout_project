from http import HTTPStatus

from fastapi.testclient import TestClient

from workout_project.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"msg": "Workout Tracker API rodando!"}
