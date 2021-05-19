"""Module of config generated for production"""

# Modules
from config.base import Config


class ProductionConfig(Config):
    """Production Config Class"""
    DEBUG = False

    # Flask env can use this data
    # local
    # development
    # production
    # testing
    ENV = FLASK_ENV = 'production'
