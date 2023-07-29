import pytest
from flask import Flask
from app.route import app, my_todos

# Helper function to create test todos
def create_todo(title, completed=False, deleted=False):
    todo = {
        "id": len(my_todos) + 1,
        "title": title,
        "completed": completed,
        "deleted": deleted
    }
    my_todos.append(todo)
    return todo

# Test fixture to set up the Flask test client
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Test cases
def test_list_todos(client):
    response = client.get('/todo/list')
    assert response.status_code == 200
    assert response.json == my_todos

def test_list_completed_todos(client):
    create_todo("Todo 1", completed=True)
    create_todo("Todo 2", completed=False)
    response = client.get('/todo/list/completed')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['completed'] is True

def test_list_deleted_todos(client):
    create_todo("Todo 1", deleted=True)
    create_todo("Todo 2", deleted=False)
    response = client.get('/todo/list/deleted')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['deleted'] is True

def test_create_todo(client):
    data = {"title": "New Todo"}
    response = client.post('/todo', json=data)
    assert response.status_code == 201
    assert "id" in response.json
    assert response.json["title"] == data["title"]

def test_get_todo_by_id(client):
    # Create a todo using the create_todo API and extract it from the response
    response = client.post('/todo', json={"title": "Test Todo"})
    assert response.status_code == 201
    new_todo = response.json

    # Now, get the todo by its ID using the API
    response = client.get(f'/todo/{new_todo["id"]}')
    assert response.status_code == 200
    assert response.json == new_todo

def test_get_todo_by_id_not_found(client):
    response = client.get('/todo/999')  # An ID that does not exist
    assert response.status_code == 404
    assert response.json["message"] == "Todo not found!"

def test_update_todo_by_id(client):
    todo = create_todo("Old Title")
    data = {"title": "New Title", "completed": True}
    response = client.put(f'/todo/{todo["id"]}', json=data)
    assert response.status_code == 200
    assert response.json["title"] == data["title"]
    assert response.json["completed"] is True

def test_delete_todo_by_id(client):
    todo = create_todo("Todo to be deleted")
    response = client.delete(f'/todo/{todo["id"]}')
    assert response.status_code == 200
    assert response.json["message"] == "Todo deleted successfully!"
    assert todo["deleted"] is True

def test_delete_todo_by_id_not_found(client):
    response = client.delete('/todo/999')  # An ID that does not exist
    assert response.status_code == 404
    assert response.json["message"] == "Todo not found!"
