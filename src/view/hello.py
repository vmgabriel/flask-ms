"""Hello Endpoint data route"""

# Libraries
from flask_restful import Resource


class Hello(Resource):
    """Hello Rest"""
    def get(self):
        """Get Data of Rest"""
        return {'hello': 'world'}


route = {
    'route': '/',
    'class': Hello
}
