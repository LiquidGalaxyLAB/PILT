# resources.py
from jsonapi.api import API
from jsonapi.resource import Resource

api = API()

@api.register
class AuthorResource(Resource):
    class Meta:
        model = 'races.race'

