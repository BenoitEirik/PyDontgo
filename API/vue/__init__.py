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
from API.controller.role_controller import RoleController
from API.controller.user_controller import UserController


# Init db & controller
database_engine = DatabaseEngine(url='sqlite:///bds.db')
database_engine.create_database()

conv_manager = ConversationController(database_engine)
conv_user_manager = ConvUserController(database_engine)
message_manager = MessageController(database_engine)
role_manager = RoleController(database_engine)
user_manager = UserController(database_engine)


# Authentification
auth = HTTPBasicAuth()

USER_DATA = { # TODO request to DB
    "admin": generate_password_hash("5GdFP7u8MYFiFc*A3dJ3TAqnBhgeqBmsjYVMaJY@PS#&bgQr")
}
# sha256 : 150000$pslYcGA8$c52a60533b934c29ad0d4132074985c9594dfe7792556f76af4c786397f4464c


@auth.verify_password
def verify(username, password):
    """
    if not (username or password):
        return False
    elif username in USER_DATA:
        return check_password_hash(USER_DATA[username], password)
    """
    # print("[help] Genrated hash :", generate_password_hash("5GdFP7u8MYFiFc*A3dJ3TAqnBhgeqBmsjYVMaJY@PS#&bgQr"), "[end]")
    if not (username or password):
        return False
    else:
        user = user_manager.get_user_by_pseudo(username)
        return check_password_hash(user['password_hash'], password)
    

# Model for register
auth_info = api_users.model('auth_info', {
    'username': fields.String('username'),
    'password': fields.String('password')
})

# API declaration
api = Api(
    # All API metadatas
    title='PyDontgo API',
    version='1.2',
    description='PyDontgo est une application de messagerie.'
)

# Namespace
api_about = Namespace('About', description='More information about PyDontgo')
api_register = Namespace('Register', description='Create a new account')
api_test = Namespace('Test', description='Do not use')


@api_about.route('/')
class API_info(Resource):
    def get(self):
        return {
            'API': '1.2',
            'access': 'authorized'
        }

@api_test.route('/')
class API_test(Resource):
    def get(self):
        user = user_manager.get_user_by_pseudo('admin')
        print("List of users: ", user)
        return {'user': 'test'}


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


# Add decorators
api_users.decorators = [auth.login_required()]
api_conversations.decorators = [auth.login_required()]

# Add Namespace
api.add_namespace(api_about, path='/api')
api.add_namespace(api_test, path='/api/test')
api.add_namespace(api_users, path='/api/users')
api.add_namespace(api_conversations, path='/api/conversations')
api.add_namespace(api_register, path='/api')

