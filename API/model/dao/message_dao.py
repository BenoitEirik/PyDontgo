from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime

from API.model.mapping.message import Message
from API.model.mapping.conv_user import ConvUser
from API.model.dao.dao import DAO

from API.exceptions import Error, ResourceNotFound


class MessageDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Message).filter_by(id=id).order_by(Message.id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Message).order_by(Message.conv_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_userId(self, user_id: int):
        try:
            return self._database_session.query(Message).join(ConvUser).filter_by(user_id=user_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_convId(self, conv_id: int):
        try:
            return self._database_session.query(Message).join(ConvUser).filter_by(conv_id=conv_id).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_newConvId(self, conv_id: int, last_call):
        try:
            return self._database_session.query(Message).join(ConvUser).filter_by(conv_id=conv_id,time_created=datetime.strptime(last_call, '%m/%d/%y %H:%M:%S')).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            message = Message(conv_user=data.get('conv_user_id'), content=data.get('content'))
            self._database_session.add(message)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return message

    def update(self, message: Message, data: dict):
        if 'content' in data:
            message.content = data['content']
        try:
            self._database_session.merge(message)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return message

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
