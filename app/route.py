from flask import Flask, jsonify, request
from .model import MyToDo, my_todos

app = Flask(__name__)


@app.route('/todo/list', methods=['GET'])
def list_todos():
    """Endpoint to get a list of all Todo items.

    Returns:
        JSON response: A list of all Todo items.
    """
    return jsonify(my_todos)


@app.route('/todo/list/completed', methods=['GET'])
def list_completed_todos():
    """Endpoint to get a list of completed Todo items.

    Returns:
        JSON response: A list of completed Todo items.
    """
    completed_todos = [todo for todo in my_todos if todo['completed']]
    return jsonify(completed_todos)


@app.route('/todo/list/deleted', methods=['GET'])
def list_deleted_todos():
    """Endpoint to get a list of deleted Todo items.

    Returns:
        JSON response: A list of deleted Todo items.
    """
    deleted_todos = [todo for todo in my_todos if todo['deleted']]
    return jsonify(deleted_todos)


@app.route('/todo', methods=['POST'])
def create_todo():
    """Endpoint to create a new Todo item.

    Request (JSON Body):
        {
            "title": "Todo item title"
        }

    Returns:
        JSON response: Details of the newly created Todo item.
    """
    data = request.get_json()
    new_todo = MyToDo(id=len(my_todos) + 1, title=data['title'])
    my_todos.append(new_todo.__dict__)
    return jsonify(new_todo.__dict__), 201


@app.route('/todo/<int:todo_id>', methods=['GET'])
def get_todo_by_id(todo_id):
    """Endpoint to get a Todo item by it's ID.

    Args:
        todo_id (int): The ID of the Todo item to retrieve.

    Returns:
        JSON response: Details of the requested Todo item.
                      If the Todo is not found, returns a 404 response.
    """
    todo = next((todo for todo in my_todos if todo['id'] == todo_id), None)
    if todo:
        return jsonify(todo)
    else:
        return jsonify({"message": "Todo not found!"}), 404


@app.route('/todo/<int:todo_id>', methods=['PUT'])
def update_todo_by_id(todo_id):
    """Endpoint to update a Todo item by its ID.

    Args:
        todo_id (int): The ID of the Todo item to update.

    Request (JSON Body):
        {
            "title": "Updated title",  # Optional
            "completed": true,   # Optional
            "deleted": false     # Optional
        }

    Returns:
        JSON response: Details of the updated Todo item.
                      If the Todo is not found, returns a 404 response.
    """
    data = request.get_json()
    todo = next((todo for todo in my_todos if todo['id'] == todo_id), None)
    if todo:
        todo['title'] = data.get('title', todo['title'])
        todo['completed'] = data.get('completed', todo['completed'])
        todo['deleted'] = data.get('deleted', todo['deleted'])
        return jsonify(todo)
    else:
        return jsonify({"message": "Todo not found!"}), 404


@app.route('/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo_by_id(todo_id):
    """Endpoint to mark a Todo item as deleted by its ID.

    Args:
        todo_id (int): The ID of the Todo item to delete.

    Returns:
        JSON response: Success message if Todo was marked as deleted.
                      If the Todo is not found, returns a 404 response.
    """
    todo = next((todo for todo in my_todos if todo['id'] == todo_id), None)
    if todo:
        todo['deleted'] = True
        return jsonify({"message": "Todo deleted successfully!"}), 200
    else:
        return jsonify({"message": "Todo not found!"}), 404
