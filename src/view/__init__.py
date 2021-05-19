"""View all data flask"""

# Libraries
from flask import Blueprint, Flask
from flask_restful import Api

# Modules
from src.view.hello import route as hello_route

APPLICATION_ROOT = '/api'


def _v0_rest(api: Api):
    """V0 REST load blueprint"""
    route_prefix = APPLICATION_ROOT + '/v0'
    routes = [
        hello_route
    ]
    for route in routes:
        api.add_resource(
            route['class'],
            route_prefix + route['route']
        )


def register_resources(app: Flask) -> Flask:
    """Register into app the resources"""
    # API v0
    api = Api(app)

    _v0_rest(api)

    return app
