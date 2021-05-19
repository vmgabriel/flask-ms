"""Base of Configuration"""


class Config:
    """Config Base Class"""
    DEBUG = False
    TESTING = False

    # Flask env can use this data
    # local
    # development
    # production
    # testing
    ENV = ''
    FLASK_ENV = ''
