from sqlalchemy import Column, String, UniqueConstraint, Integer
from API.model.mapping import Base


class Conversation(Base):
    __tablename__ = 'conversation'
    __tableArgs__ = (UniqueConstraint('name'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Member(%s %s)>" % (self.id, self.name)

    def to_dictionary(self):
        return dict(id=self.id, name=self.name)
