"""Config local Config"""

# Modules
from config.base import Config


class TestingConfig(Config):
    """Config Testing"""
    TESTING = True

    # Flask env can use this data
    # local
    # development
    # production
    # testing
    ENV = FLASK_ENV = 'testing'
