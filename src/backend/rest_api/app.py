import os

from flask import Flask
from rest_api.api import api, blueprint
from rest_api.controller.todo_controller import api as todo_ns
from rest_api.config import config_by_name

# add namespaces
api.add_namespace(todo_ns, path="/todo")

app = Flask(__name__)
app.config.from_object(config_by_name[os.getenv("ENVIRONMENT") or "dev"])
app.register_blueprint(blueprint)
app.app_context().push()
