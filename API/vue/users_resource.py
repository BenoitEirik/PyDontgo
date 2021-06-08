from flask_restx import Namespace, Resource, fields

api_users = Namespace('Users', description='Gestion des utilisateurs')


@api_users.route('/')
class Users(Resource):
    def get(self):
        return {
            'users': ['Olaf', 'Flamb3rym', 'Venice', 'Coco']
        }

    def post(self):
        pass


@api_users.route('/<string:id_user>')
class User(Resource):
    def get(self, id_user):
        if user in my_users:
            # TODO retrieve data of a user in function of his id_user
            return {
                'id': '#user1234',
                'username': 'Olaf',
            }
        else:
            return {'error': '404'}

