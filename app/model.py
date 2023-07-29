class MyToDo:
    def __init__(self, id, title, completed=False, deleted=False):
        self.id = int(id)
        self.title = title
        self.completed = completed
        self.deleted = deleted

# in-memory database for storing all todos
my_todos = []
