from flask_restx import Namespace, Resource, fields

api_conversations = Namespace('Conversations', description='Gestion des conversations')


# Model for PUT json
msg_model = api_conversations.model('msg_model', {
    'id': fields.Integer(4),
    'author': fields.String('author'),
    'content': fields.String('my_msg')
})


# Conversation requests
@api_conversations.route('/list_convs/<string:id_user>')
class ListConversations(Resource):
    def get(self, id_user):
        # TODO Example of json to return en fonction de id_user

        test = [
            {
                'id': '#conv2345',
                'name': 'Collin',
                'users': ['Olaf','Collin']
            },
            {
                'id': '#conv1234',
                'name': 'Physique',
                'users': ['Olaf','Collin','Shraf','Venice']
            }
        ]
        return test

@api_conversations.route('/conv/<string:id_conv>/<string:type>/<string:timestamp>')
class Conversation(Resource):
    def get(self, id_conv, type, timestamp):
        # TODO Example of json to return in function of id_conv, type and -->timestamp<--
        if type == "get_msg":
            test = [
                {
                    'id': 1,
                    'id_author': '#user1234',
                    'content': 'Yo ça va ?',
                    'timestamp': '1234456789'
                },
                {
                    'id': 2,
                    'id_author': '#user4321',
                    'content': 'Yes et toi ?',
                    'timestamp': '987654321'
                }
            ]
            return test
        elif type == "modify_msg":
            pass

    @api_conversations.expect(msg_model)
    def put(self, id_conv, type):
        if(type == 'add_msg'):
            list_msg.append(api_conversations.payload)
        return {'status': 'Reiceved message'}
        
