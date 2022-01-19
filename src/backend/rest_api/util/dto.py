from flask_restx import Namespace, fields


class TodoDto:
    api = Namespace("todos", description="TODO operations")
    todo = api.model(
        "Todo", {"task": fields.String(required=True, description="The task details")}
    )
    listed_todo = api.model(
        "ListedTodo",
        {
            "id": fields.String(required=True, description="The todo ID"),
            "todo": fields.Nested(todo, description="The Todo"),
        },
    )
