# ToDo List Management App

This is a simple HTTP API backend app for managing ToDo items. It allows you to perform CRUD operations on ToDo items, view all items, view completed items and view deleted items. The app is built using Python and Flask.

## Getting Started

To get started with the app, follow the instructions below to set up and run the application.

### Prerequisites

- Python 3.9 or higher
- Docker (optional, for running the app using Docker Compose)

### Installation

Clone the repository to your local machine:
```
gh repo clone sonalvar/todo_app
```

### Create a virtual environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate    # On Windows, use: venv\Scripts\activate
```

### Install the required packages:
```
pip install -r requirements.txt
```

## Running the App
#### Using Python
To run the app using Python, execute the following command:

```
python main.py
```
The app will start, and you can access it at: http://127.0.0.1:8090

#### Using Docker Compose
If you prefer running the app using Docker Compose, make sure you have Docker installed and running on your machine. Then, execute the following command:

```
docker-compose up
```
The app will be accessible at: http://127.0.0.1:8090

## API Endpoints
- **GET /todo/list**: Get a list of all ToDo items.
- **GET /todo/list/completed**: Get a list of completed ToDo items.
- **GET /todo/list/deleted**: Get a list of deleted ToDo items.
- **POST /todo**: Create a new ToDo item. Send the title as a JSON payload.
- **GET /todo/<int:todo_id>**: Get a specific ToDo item by ID.
- **PUT /todo/<int:todo_id>**: Update a specific ToDo item by ID. Send the title (optional), completed (optional), and deleted (optional) as a JSON payload.
- **DELETE /todo/<int:todo_id>**: Delete a specific ToDo item by ID.

## Running Tests
To run the unit tests for the app, use the following command:
```
pytest app/tests
```
The test cases should be detected and executed successfully.
