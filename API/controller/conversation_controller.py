from API.model.dao.conversation_dao import ConversationDAO


class ConversationController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_conversations(self):
        with self._database_engine.new_session() as session:
            conversations = ConversationDAO(session).get_all()
            conversations_data = [conversation.to_dictionary() for
                                  conversation in conversations]
        return conversations_data

    def search_conversation_by_name(self, name):
        with self._database_engine.new_session() as session:
            conversations_dao = ConversationDAO(session)
            conversation = conversations_dao.get_by_name(name)
            return conversation.to_dictionary()

    def delete_conversation(self, name):
        with self._database_engine.new_session() as session:
            conversations_dao = ConversationDAO(session)
            conversation = conversations_dao.get_by_name(name)
            conversations_dao.delete(conversation)
