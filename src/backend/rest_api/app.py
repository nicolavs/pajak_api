from flask import Flask
from rest_api.api import api, blueprint
from rest_api.controller.todo_controller import api as todo_ns

# add namespaces
api.add_namespace(todo_ns, path="/todo")

app = Flask(__name__)
app.register_blueprint(blueprint)
app.app_context().push()
