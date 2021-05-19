"""Flask Init Configuration"""

# Configurations
from config import config

# Libraries
from flask import Flask


app = Flask(__name__, instance_relative_config=True)


def create_app(env_name: str) -> Flask:
    """
    Create a app flask with env_name

    env_name can be:
    - local (default)
    - development
    - production
    - testing
    """
    app.config.from_object(
        config[env_name]
    )

    return app
