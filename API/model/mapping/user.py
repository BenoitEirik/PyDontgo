from sqlalchemy import Column, String, UniqueConstraint, Date, Integer
from sqlalchemy import *
from API.model.database import DatabaseEngine
from API.model.mapping import Base


class User(Base):
    __tablename__ = 'user'
    __tableArgs__ = (UniqueConstraint('username'),)

    id = Column(Integer, primary_key=True, autoincrement=True)

    lastname = Column(String(50), nullable=False)
    firstname = Column(String(50), nullable=False)
    username = Column(String(20), nullable=False, index=True)
    password_hash = Column(String(128), nullable=False)


    def __repr__(self):
        return "<Member(%s %s , %s)>" % (self.firstname, self.lastname.upper(), self.username)

    def to_dictionary(self):
        return dict(id=self.id, lastname=self.lastname, firstname=self.firstname,
                    username=self.username, password_hash=self.password_hash)
