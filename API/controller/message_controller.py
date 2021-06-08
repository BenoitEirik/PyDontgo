from API.model.dao.message_dao import MessageDAO
from API.exceptions import Error


class MessageController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_message(self):
        # Permet de récupérer tous les messages envoyées depuis la creation
        # (pas conseillé mdr)
        with self._database_engine.new_session() as session:
            messages = MessageDAO(session).get_all()
            messages_data = [message.to_dictionary() for message in
                             messages]
        return messages_data

    def list_user_messages(self, user_id):
        # Permet d'afficher les messages d'un utilisateurs
        with self._database_engine.new_session() as session:
            user_messages = MessageDAO(session).get_by_userId(user_id)
            users_messages_data = [user_message.to_dictionary() for
                                   user_message in user_messages]
        return users_messages_data

    def list_conv_messages(self, conv_id):
        # Permet d'afficher les messages d'une conversation
        with self._database_engine.new_session() as session:
            conv_messages = MessageDAO(session).get_by_convId(conv_id)
            conv_messages_data = [conv_message.to_dictionary() for
                                  conv_message in conv_messages]
        return conv_messages_data

    def get_message(self, message_id):
        # Permet de récupérer un message
        with self._database_engine.new_session() as session:
            message = MessageDAO(session).get(message_id)
            message_data = message.to_dictionary()
        return message_data

    def create_message(self, data):
        # Permet de creer un message
        try:
            with self._database_engine.new_session() as session:
                message = MessageDAO(session).create(data)
                message_data = message.to_dictionary()
                return message_data
        except Error as e:
            raise e

    def delete_message(self, message_id):
        with self._database_engine.new_session() as session:
            message_dao = MessageDAO(session)
            message = message_dao.get(message_id)
            message_dao.delete(message)
