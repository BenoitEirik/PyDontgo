from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from API.model.mapping.user import User
from API.model.dao.dao import DAO
from API.exceptions import Error, ResourceNotFound


class UserDAO(DAO):
    """
    User Mapping DAO
    """

    def __init__(self, database_session):
        super().__init__(database_session)

    def get(self, id):
        try:
            return self._database_session.query(User).filter_by(id=id).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_all(self):
        try:
            return self._database_session.query(User).order_by(User.lastname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_pseudo(self, pseudo: str):
        try:
            return self._database_session.query(User).filter_by(pseudo=pseudo).one()
        except NoResultFound:
            raise ResourceNotFound()

    def get_by_name(self, lastname: str):
        try:
            return self._database_session.query(User).filter_by(lastname=lastname)\
                .order_by(User.firstname).all()
        except NoResultFound:
            raise ResourceNotFound()

    def create(self, data: dict):
        try:
            user = User(firstname=data.get('firstname'), lastname=data.get('lastname'), pseudo=data.get('pseudo'), password=data.get('password'))
            self._database_session.add(user)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Member already exists")
        return user

    def update(self, user: User, data: dict):
        if 'firstname' in data:
            user.firstname = data['firstname']
        if 'lastname' in data:
            user.lastname = data['lastname']
        if 'pseudo' in data:
            user.pseudo = data['pseudo']
        if 'password' in data:
            user.password = data['password']
        try:
            self._database_session.merge(user)
            self._database_session.flush()
        except IntegrityError:
            raise Error("Error data may be malformed")
        return user

    def delete(self, entity):
        try:
            self._database_session.delete(entity)
        except SQLAlchemyError as e:
            raise Error(str(e))
