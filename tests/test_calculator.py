
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_addition():
    response = client.post(
        "/calculate",
        json={"number1": 10, "number2": 5, "operation": "add"}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 15


def test_subtraction():
    response = client.post(
        "/calculate",
        json={"number1": 10, "number2": 5, "operation": "subtract"}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 5


def test_multiplication():
    response = client.post(
        "/calculate",
        json={"number1": 10, "number2": 5, "operation": "multiply"}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 50


def test_division():
    response = client.post(
        "/calculate",
        json={"number1": 10, "number2": 5, "operation": "divide"}
    )

    assert response.status_code == 200
    assert response.json()["result"] == 2


def test_division_by_zero():
    response = client.post(
        "/calculate",
        json={"number1": 10, "number2": 0, "operation": "divide"}
    )

    assert response.status_code == 400
