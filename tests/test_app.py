import json
from src.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bem-vindo" in response.data

def test_add_and_get_tasks():
    client = app.test_client()
    task_data = {"title": "Estudar Flask", "description": "Aprender API simples"}
    response = client.post('/tasks', data=json.dumps(task_data), content_type='application/json')
    assert response.status_code == 201

    get_response = client.get('/tasks')
    data = json.loads(get_response.data)
    assert len(data) > 0
    assert data[0]["title"] == "Estudar Flask"
