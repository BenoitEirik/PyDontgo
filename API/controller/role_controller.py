from API.model.dao.role_dao import RoleDAO


class RoleController:

    def __init__(self, database_engine):
        self._database_engine = database_engine

    def list_role(self):
        # lister tous les rôles
        with self._database_engine.new_session() as session:
            role = RoleDAO(session).get_all()
            role_data = [_role.to_dictionary() for _role in role]
        return role_data

    def get_role_by_name(self, name):
        with self._database_engine.new_session() as session:
            role_dao = RoleDAO(session)
            role = role_dao.get_by_name(name)
            return role.to_dictionary()

    def get_role(self, role_id):
        with self._database_engine.new_session() as session:
            role = RoleDAO(session).get(role_id)
            role_data = role.to_dictionary()
        return role_data

    # 2205
