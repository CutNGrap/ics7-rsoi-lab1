from fastapi.testclient import *
from main import app, engine
from sqlmodel import SQLModel

client = TestClient(app)

SQLModel.metadata.create_all(engine)

def test_get_persons():
    response = client.get("/api/v1/persons")
    assert response.status_code == 200
    for person in response.json():
        assert person.keys() == set(["id", "name", "age", "address", "work"])

def test_positive_add_person():
    response = client.post("/api/v1/persons", json={"name": "Alex", "age": 13, "address": "Street", "work": "Street"})
    assert response.status_code == 201
    assert response.headers["Location"].split("/")[:-1] == ["", "api", "v1", "persons"]

def test_negative_add_person():
    response = client.post("/api/v1/persons", json={"work": "Street"})
    assert response.status_code == 400
    assert response.json()["message"] == "what"

def test_positive_patch_person():
    response = client.post("/api/v1/persons", json={"name": "Alex", "age": 13, "address": "Street", "work": "Street"})
    assert response.status_code == 201
    assert response.headers["Location"].split("/")[:-1] == ["", "api", "v1", "persons"]
    person_id = response.headers["Location"].split("/")[-1]
    response = client.patch(f"api/v1/persons/{person_id}", json={"name": "Xey", "age": 60})
    assert response.status_code == 200
    assert response.json() == {"id": int(person_id), "name": "Xey", "age": 60, "address": "Street", "work": "Street"}


def test_negative_patch_person():
    response = client.patch(f"api/v1/persons/100", json={"name": "Alex", "age": 60})
    assert response.status_code == 404
