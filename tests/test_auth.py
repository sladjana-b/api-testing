import pytest
from utils.api_client import ApiClient

client = ApiClient(base_url="https://api.restful-api.dev")


def test_create_object_success():
    payload = {
        "name": "Sladjana Test Object",
        "data": {
            "field": "value"
        }
    }

    response = client.post("/objects", json=payload)

    # restful-api.dev vraća 200 OK pri kreiranju
    assert response.status_code == 200

    data = response.json()

    assert data["name"] == payload["name"]
    assert "id" in data
    assert isinstance(data["id"], str)


def test_create_object_missing_field():
    # restful-api.dev NE radi validaciju
    # i kreira objekat čak i ako nedostaju polja
    payload = {
        "data": {
            "cpu": "Intel"
        }
    }

    response = client.post("/objects", json=payload)

    # vraća 200 OK čak i bez name
    assert response.status_code == 200

    data = response.json()
    assert "id" in data
