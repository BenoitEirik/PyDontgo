from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from API.model.mapping.conversation import Conversation
from API.model.dao.dao import DAO

from API.exceptions import Error, ResourceNotFound


class ConversationDAO(DAO):
    """
    Member Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(Conversation).filter_by(id=id).order_by(Conversation.name).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(Conversation).order_by(Conversation.name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, name: str):
        try:
            return self._database_session.query(Conversation).filter_by(name=name).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            conversation = Conversation(name=data.get('name'))
            self._database_session.add(conversation)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return conversation

    def update(self, conversation: Conversation, data: dict):
        if 'name' in data:
            conversation.name = data['name']
        try:
            self._database_session.merge(conversation)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return conversation

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
