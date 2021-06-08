from flask_restx import Api, Namespace, Resource, fields
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from API.vue.users_resource import api_users
from API.vue.conversations_resource import api_conversations


from API.model.database import DatabaseEngine
from API.model.mapping import role, user, conv_user, conversation, message
from API.controller.conversation_controller import ConversationController
from API.controller.conv_user_controller import ConvUserController
from API.controller.message_controller import MessageController
from API.controller.user_controller import UserController

"""
# Init db
database_engine = DatabaseEngine(url='sqlite:///bds.db')
database_engine.create_database()
user_manager = UserController(database_engine)
conv_user_manger = ConvUserController(database_engine)
conv_manager = ConversationController(database_engine)
"""

# Authentification
auth = HTTPBasicAuth()

USER_DATA = { # TODO request to DB
    "admin": generate_password_hash("5GdFP7u8MYFiFc*A3dJ3TAqnBhgeqBmsjYVMaJY@PS#&bgQr")
}
# sha256 : 150000$pslYcGA8$c52a60533b934c29ad0d4132074985c9594dfe7792556f76af4c786397f4464c

@auth.verify_password
def verify(username, password):
    if not (username or password):
        return False
    elif username in USER_DATA:
        return check_password_hash(USER_DATA[username], password)
    """
    user = user_manager.get_user_by_pseudo(username)
    if not (username and password):
        return False
    return check_password_hash(user.password, password)
    """

# API declaration
api = Api(
    # All API metadatas
    title='PyDontgo API',
    version='1.2',
    description='PyDontgo est une application de messagerie.'
)

api_about = Namespace('About', description='More information about PyDontgo')


@api_about.route('/')
class API_info(Resource):
    def get(self):
        return {
            'birthday': '10/04/2021',
            'creator': ['SERGENT Olaf-Marie', 'Flamb3rym', 'Venice', 'Coco']
        }



# Model for register
auth_info = api_users.model('auth_info', {
    'username': fields.String('username'),
    'password': fields.String('password')
})

api_register = Namespace('Register', description='Create a new account')


@api_register.route('/register')
class Authentification(Resource):
    @api_users.expect(auth_info)
    def put(self, type):
        request = api_users.payload
        username = request['username']
        password = request['password']
        # TODO check if user don't exist + saving in BBD + return json in function of invalid and valid variable
        invalid = {'error': '404'}
        valid = {'registering': 'success'}



api_users.decorators = [auth.login_required()]
api_conversations.decorators = [auth.login_required()]

api.add_namespace(api_about, path='/api')
api.add_namespace(api_users, path='/api/users')
api.add_namespace(api_conversations, path='/api/conversations')
api.add_namespace(api_register, path='/api')

