import pytest
from utils.api_client import ApiClient
from utils.helpers import validate_keys

client = ApiClient(base_url="https://api.restful-api.dev")


def test_get_objects_list():
    response = client.get("/objects")
    assert response.status_code == 200

    json_data = response.json()

    assert isinstance(json_data, list)
    assert len(json_data) > 0

    first = json_data[0]
    expected = ["id", "name", "data"]
    validate_keys(first, expected)


def test_get_single_object():
    response = client.get("/objects/1")
    assert response.status_code == 200

    data = response.json()

    assert "id" in data
    assert "name" in data
    assert "data" in data


def test_single_object_not_found():
    response = client.get("/objects/999999999")
    assert response.status_code == 404


def test_create_object_success():
    payload = {
        "name": "Created from tests",
        "data": {
            "x": 123
        }
    }

    response = client.post("/objects", json=payload)
    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert "id" in data
