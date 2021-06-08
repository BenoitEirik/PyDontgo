from sqlalchemy import Column, String, UniqueConstraint, Integer
from API.model.mapping import Base


class Role(Base):
    __tablename__ = 'role'
    __tableArgs__ = (UniqueConstraint('name'),)

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return "<Role(%s %s)>" % (self.id, self.name)

    def to_dictionary(self):
        return dict(id=self.id, firstName=self.name)
