from fastapi.testclient import TestClient
from main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

client = TestClient(app)

def test_create_company(db):
    company_data = {
        "name": "Ribeiros",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiros@example.com",
        "phone": "1234567890"
    }

    response = client.post("/companies/", json=company_data)

    assert response.status_code == 201  
    assert response.json()["name"] == company_data["name"]
    assert response.json()["cnpj"] == company_data["cnpj"]
    assert response.json()["address"] == company_data["address"]
    assert response.json()["email"] == company_data["email"]
    assert response.json()["phone"] == company_data["phone"]

def test_read_company():
    response = client.get("/companies/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Ribeiros",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiros@example.com",
        "phone": "1234567890"
    }

def test_update_company():
    update_data = {
        "name": "Ribeiros Updated",
        "cnpj": "12345678987324",
        "address": "Novo Endereço",
        "email": "ribeiroCompany@example.com", 
        "phone": "0987654321"
    }

    response = client.patch("/companies/1", json=update_data)

    assert response.status_code == 200 
    assert response.json()["name"] == update_data["name"]
    assert response.json()["email"] == update_data["email"]
    assert response.json()["phone"] == update_data["phone"]

def test_delete_company():
    response = client.delete("/companies/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Company deleted"}

def test_create_obligation(db):
    company_data = {
        "name": "Ribeiros",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiros@example.com",
        "phone": "1234567890"
    }
    company_response = client.post("/companies/", json=company_data)
    company_id = company_response.json()["id"]

    obligation_data = {
        "name": "Obligation 1",
        "frequency": "monthly",
        "company_id": company_id
    }

    response = client.post("/obligations/", json=obligation_data)

    assert response.status_code == 201
    assert response.json()["name"] == obligation_data["name"]
    assert response.json()["frequency"] == obligation_data["frequency"]
    assert response.json()["company_id"] == obligation_data["company_id"]

def test_read_obligation():
    response = client.get("/obligations/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Obligation 1",
        "frequency": "monthly",
        "company_id": 1
    }

def test_update_obligation():
    update_data = {
        "name": "Obligation 1",
        "frequency": "annually",
        "company_id": 1
    }

    response = client.patch("/obligations/1", json=update_data)

    assert response.status_code == 200
    assert response.json()["frequency"] == update_data["frequency"]

def test_delete_obligation():
    response = client.delete("/obligations/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Obligation deleted"}
