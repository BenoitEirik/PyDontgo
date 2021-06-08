from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from API.model.mapping.role import Role
from API.model.dao.dao import DAO

from API.exceptions import Error, ResourceNotFound


class RoleDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Role).filter_by(id=id).order_by(Role.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Role).order_by(Role.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Role).filter_by(name=name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            role = Role(name=data.get('name'))
            self._database_session.add(role)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return role

    def update(self, role: Role, data: dict):
        if 'name' in data:
            role.name = data['name']
        try:
            self._database_session.merge(role)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return role

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
