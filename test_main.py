from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_company():
    response = client.post("/companies/", json={"name": "Test Company", "cnpj": "12345678901234", "address": "Test Street", "email": "test@test.com", "phone": "1234567890"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Company"

def test_read_company():
    response = client.get("/companies/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1