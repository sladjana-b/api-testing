This project demonstrates a simple and clean API testing framework built using Python, Pytest, and the Requests library.
The tests cover CRUD operations on the public API:
https://api.restful-api.dev/

The goal is to practice REST API validation, JSON structure checks, status code verification, and basic test framework design.

Features:

Custom ApiClient abstraction (GET, POST, PUT, PATCH, DELETE)
CRUD tests on /objects endpoint
Positive & negative test scenarios
JSON response validation
Status code verification
Full Pytest structure
Easily extendable for more endpoints
Perfect base for future automation

Technology Stack: Python 3, Pytest, Requests library, REST API (public demo API)

Running the tests
1. Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate
2. Installing dependencies:
pip install -r requirements.txt
3. Running all TCs:
pytest -v

Example Test Flow
-Create an object
-Update full object (PUT)
-Patch partial data (PATCH)
-Delete object and verify 404
-Validate JSON response fields
-Check status codes (200, 201, 404)

Notes:
This repository is intended as a lightweight API testing practice project and a minimal test framework that can be expanded with:
-fixtures
-environment configs
-parallel execution
-CI integration
-test data factories

This mini-framework demonstrates strong understanding of:
-API testing fundamentals
-REST operations
-Pytest project structure
-JSON validation
-Negative scenario testing
-Clean code & modular design

<p align="center">
  <img src="thumbnail.png" width="500">
</p>


