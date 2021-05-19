"""Config local Config"""

# Modules
from config.base import Config


class LocalConfig(Config):
    """Config Local"""
    DEBUG = True
    TESTING = True

    # Flask env can use this data
    # local
    # development
    # production
    # testing
    ENV = FLASK_ENV = 'local'
