from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_company(): 
    company_data = {
        "name": "Ribeiro's",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiros@example.com",
        "phone": "1234567890"
    }

    response = client.post("/companies/", json=company_data)

    assert response.status_code == 201
    assert response.json() == company_data

def test_read_company():
    response = client.get("/companies/1")

    assert response.status_code == 200
    assert response.json() == {
        "name": "Ribeiro's",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiros@example.com",
        "phone": "1234567890"
    }

def test_update_company():
    update_data = {
        "name": "Ribeiro's",
        "cnpj": "12345678987324",
        "address": "Loteamento Agamenon",
        "email": "ribeiroCompany@example.com", 
        "phone": "1234567890"
    }

    response = client.patch("/companies/1", json=update_data)

    assert response.status_code == 200
    assert response.json() == update_data

def test_delete_company():
    response = client.delete("/companies/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Company deleted"}

def test_create_obligation():
    obligation_data = {
        "name": "Obligation 1",
        "frequency": "monthly",
        "company_id": 1
    }

    response = client.post("/obligations/", json=obligation_data)

    assert response.status_code == 201
    assert response.json() == obligation_data

def test_read_obligation():
    response = client.get("/obligations/1")

    assert response.status_code == 200
    assert response.json() == {
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
    assert response.json() == update_data

def test_delete_obligation():
    response = client.delete("/obligations/1")

    assert response.status_code == 200
    assert response.json() == {"message": "Obligation deleted"}