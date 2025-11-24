import pytest
from utils.api_client import ApiClient

client = ApiClient(base_url="https://api.restful-api.dev")

# -----------------------------
# CREATE OBJECT
# -----------------------------
def test_create_object_success():
    payload = {
        "name": "Test Device",
        "data": {
            "cpu": "Intel",
            "ram": "16GB"
        }
    }

    response = client.post("/objects", json=payload)

    assert response.status_code == 200

    data = response.json()

    # Validate returned fields
    assert data["name"] == payload["name"]
    assert "id" in data
    assert "createdAt" in data


# -----------------------------
# UPDATE OBJECT (PUT)
# -----------------------------
def test_update_object_put():
    # First create an object
    payload = {
        "name": "Laptop",
        "data": {"brand": "Dell"}
    }

    created = client.post("/objects", json=payload).json()
    object_id = created["id"]

    # Now update the object
    updated_payload = {
        "name": "Laptop Updated",
        "data": {"brand": "HP"}
    }

    response = client.put(f"/objects/{object_id}", json=updated_payload)

    assert response.status_code == 200
    updated_data = response.json()

    # Validate updated fields
    assert updated_data["name"] == updated_payload["name"]
    assert updated_data["data"]["brand"] == updated_payload["data"]["brand"]

# -----------------------------
# PARTIAL UPDATE (PATCH)
# -----------------------------
def test_patch_object():
    # Create initial object
    payload = {
        "name": "Phone",
        "data": {"model": "Samsung"}
    }

    created = client.post("/objects", json=payload).json()
    object_id = created["id"]

    # Prepare partial update
    patch_payload = {
        "data": {"model": "iPhone"}
    }

    response = client.patch(f"/objects/{object_id}", json=patch_payload)
    assert response.status_code == 200

    patched = response.json()

    # Validate partially updated field
    assert patched["data"]["model"] == "iPhone"

# -----------------------------
# DELETE OBJECT
# -----------------------------
def test_delete_object():
    # Create object to delete
    payload = {
        "name": "Temporary Device",
        "data": {"voltage": "5V"}
    }

    created = client.post("/objects", json=payload).json()
    object_id = created["id"]

    # Perform delete
    response = client.delete(f"/objects/{object_id}")
    assert response.status_code == 200 or response.status_code == 204

    # Confirm it no longer exists
    check = client.get(f"/objects/{object_id}")
    assert check.status_code == 404
