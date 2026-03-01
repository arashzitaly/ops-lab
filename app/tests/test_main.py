from fastapi.testclient import TestClient

from ops_lab.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_hello_default():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"": "Hello, world!"}

def test_hello_with_name():
    response = client.get("/hello?name=DevOps")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, DevOps!"}