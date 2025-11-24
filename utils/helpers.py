def validate_keys(data: dict, expected_keys: list):
    """
    Validates that all expected keys exist in the JSON response.
    """
    for key in expected_keys:
        if key not in data:
            raise AssertionError(f"Missing key in response JSON: '{key}'")


def validate_types(data: dict, expected_types: dict):
    """
    Validates that JSON fields are of expected types.

    expected_types example:
    {
        "id": int,
        "email": str
    }
    """
    for key, expected_type in expected_types.items():
        if key not in data:
            raise AssertionError(f"Missing key for type validation: '{key}'")

        if not isinstance(data[key], expected_type):
            raise AssertionError(
                f"Key '{key}' has wrong type: expected {expected_type}, got {type(data[key])}"
            )
