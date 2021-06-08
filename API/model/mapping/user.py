from sqlalchemy import Column, String, UniqueConstraint, Date, Integer
from sqlalchemy import *
from API.model.database import DatabaseEngine
from API.model.mapping import Base


class User(Base):
    __tablename__ = 'user'
    __tableArgs__ = (UniqueConstraint('pseudo'),)

    id = Column(Integer, primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    pseudo = Column(String(20), nullable=False, index=True)
    password = Column(String(128), nullable=False)


    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dictionary(self):
        return dict(id=self.id, firstname=self.firstname, lastname=self.lastname,
                    pseudo=self.pseudo, password=self.password)
