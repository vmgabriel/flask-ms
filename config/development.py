"""config python development"""

# Modules
from config.base import Config


class DevelopmentConfig(Config):
    """Config Testing"""
    TESTING = True
    DEBUG = True

    # Flask env can use this data
    # local
    # development
    # production
    # testing
    ENV = FLASK_ENV = 'development'
