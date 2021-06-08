from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from API.model.mapping.conv_user import ConvUser
from API.model.dao.dao import DAO

from API.exceptions import Error, ResourceNotFound


class ConvUserDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(ConvUser).filter_by(id=id).order_by(ConvUser.conv_id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(ConvUser).order_by(ConvUser.conv_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_userId(self, user_id: int):
        try:
            return self._database_session.query(ConvUser).filter_by(user_id=user_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_convId(self, conv_id: int):
        try:
            return self._database_session.query(ConvUser).filter_by(conv_id=conv_id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            convUser = ConvUser(conv_id=data.get('conv_id'), user_id=data.get('user_id'), role_id=data.get('role_id'))
            if 'nickname' in data:
                convUser.nickname = data['nickname']
            self._database_session.add(convUser)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return convUser

    def update(self, convUser: ConvUser, data: dict):
        if 'name' in data:
            convUser.nickname = data['nickname']
        if 'role_id' in data:
            convUser.nickname = data['role_id']
        try:
            self._database_session.merge(convUser)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return convUser

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
