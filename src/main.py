"""Start applicacion base"""

# Libraries
from typing import Any

# Modules
from src import flask
from src.view import register_resources


def suma(a: int, b: int) -> int:
    """Sum the data"""
    return a + b


def create_server(framework_name: str, env_data: str) -> Any:
    """Create the app configuration"""
    if framework_name == 'flask':
        flask_server = flask.create_app(env_data)
        return register_resources(flask_server)
    raise Exception(f'Not Valid Framework name - {framework_name}')
