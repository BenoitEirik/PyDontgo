from API.model.dao.conv_users_dao import ConvUserDAO


class ConvUserController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_conv(self):
        # Permet de lister les conversations
        with self._database_engine.new_session() as session:
            conv = ConvUserDAO(session).get_all()
            conv_data = [_conv.to_dictionary() for _conv in conv]
        return conv_data

    def list_conv_by_user_id(self, user_id: int):
        # Permet de lister les conversation d'un utilisateur
        with self._database_engine.new_session() as session:
            conv_dao = ConvUserDAO(session)
            conv = conv_dao.get_by_userId(user_id)
            conv_data = [_conv.to_dictionary() for _conv in conv]
        return conv_data

    def search_conv_by_id(self, conv_id: int):
        # Permet de rechercher une conversation à partir de son ID
        with self._database_engine.new_session() as session:
            conv_dao = ConvUserDAO(session)
            conv = conv_dao.get_by_convId(conv_id)
            return conv.to_dicionary()

    def get_conv_user(self, conv_user_id):
        with self._database_engine.new_session() as session:
            conv_user = ConvUserDAO(session).get(conv_user_id)
            conv_user_data = conv_user.to_dicionary()
        return conv_user_data

    def get_users_by_conv(self, conv_id):
        # permet de lister les membres d'une conversation
        with self._database_engine.new_session() as session:
            conv_dao = ConvUserDAO(session)
            conv = conv_dao.get_by_convId(conv_id)
            members_data = [_conv.to_dictionary() for _conv in conv]
        return members_data
