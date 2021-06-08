import re
from API.model.dao.user_dao import UserDAO
from API.exceptions import Error, InvalidData


class UserController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_users(self):
        with self._database_engine.new_session() as session:
            users = UserDAO(session).get_all()
            users_data = [user.to_dictionary() for user in users]
        return users_data

    def get_user(self, user_id):
        with self._database_engine.new_session() as session:
            member = UserDAO(session).get(user_id)
            member_data = member.to_dictionary()
        return member_data

    def get_user_by_pseudo(self, pseudo: str):
        with self._database_engine.new_session() as session:
            member = UserDAO(session).get_by_pseudo(pseudo)
            member_data = member.to_dictionary()
        return member_data

    def create_user(self, data):
        self._check_profile_data(data)
        try:
            with self._database_engine.new_session() as session:
                # Save member in database
                user = UserDAO(session).create(data)
                user_data = user.to_dictionary()
                return user_data
        except Error as e:
            # log error
            raise e

    def update_user(self, user_id, user_data):

        self._check_profile_data(user_data, update=True)
        with self._database_engine.new_session() as session:
            user_dao = UserDAO(session)
            user = user_dao.get(user_id)
            user = user_dao.update(user, user_data)
            return user.to_dict()

    def delete_user(self, user_id):

        with self._database_engine.new_session() as session:
            user_dao = UserDAO(session)
            user = user_dao.get(user_id)
            user_dao.delete(user)

    def _check_profile_data(self, data, update=False):
        name_pattern = re.compile("^[\S-]{2,50}$")
        email_pattern = re.compile("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")
        mandatories = {
            'firstname': {"type": str, "regex": name_pattern},
            'lastname': {"type": str, "regex": name_pattern},
            'email': {"type": str, "regex": email_pattern}
        }
        for mandatory, specs in mandatories.items():
            if not update:
                if mandatory not in data or data[mandatory] is None:
                    raise InvalidData("Missing value %s" % mandatory)
            else:
                if mandatory not in data:
                    continue
            value = data[mandatory]
            if "type" in specs and not isinstance(value, specs["type"]):
                raise InvalidData("Invalid type %s" % mandatory)
            if "regex" in specs and isinstance(value, str) and not re.match(specs["regex"], value):
                raise InvalidData("Invalid value %s" % mandatory)


