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

def test_add_person():
    response = client.post("/api/v1/persons", json={"name": "Ivan", "age": 25, "address": "Tverskaya", "work": "Google"})
    assert response.status_code == 201
    assert response.headers["Location"].split("/")[:-1] == ["", "api", "v1", "persons"]

def test_bad_add_person():
    response = client.post("/api/v1/persons", json={"age": 25, "address": "Tverskaya", "work": "Google"})
    assert response.status_code == 400
    assert response.json()["message"] == "what"

def test_delete_person():
    response = client.delete("/api/v1/persons/100")
    assert response.status_code == 204

def test_patch_person():
    response = client.post("/api/v1/persons", json={"name": "Ivan", "age": 25, "address": "Tverskaya", "work": "Google"})
    assert response.status_code == 201
    assert response.headers["Location"].split("/")[:-1] == ["", "api", "v1", "persons"]
    person_id = response.headers["Location"].split("/")[-1]
    response = client.patch(f"api/v1/persons/{person_id}", json={"name": "Vasilii", "age": 50})
    assert response.status_code == 200
    assert response.json() == {"id": int(person_id), "name": "Vasilii", "age": 50, "address": "Tverskaya", "work": "Google"}


def test_bad_patch_person():
    response = client.patch(f"api/v1/persons/100", json={"name": "Vasilii", "age": 50})
    assert response.status_code == 404
