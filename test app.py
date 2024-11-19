import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.post('/add', json={'a': 5, 'b': 3})
    assert response.status_code == 200
    assert response.get_json()['result'] == 8

def test_subtract(client):
    response = client.post('/subtract', json={'a': 10, 'b': 7})
    assert response.status_code == 200
    assert response.get_json()['result'] == 3

def test_multiply(client):
    response = client.post('/multiply', json={'a': 4, 'b': 6})
    assert response.status_code == 200
    assert response.get_json()['result'] == 24

def test_divide(client):
    response = client.post('/divide', json={'a': 20, 'b': 4})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5.0

def test_divide_by_zero(client):
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Division by zero'
