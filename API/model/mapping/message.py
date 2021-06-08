from sqlalchemy import Column, Integer, ForeignKey, Text, DateTime
from sqlalchemy.sql import func
import datetime
from API.model.mapping import Base


class Message(Base):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    conv_user = Column(Integer, ForeignKey('conv_user.id'))
    content = Column(Text)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    def __repr__(self):
        return "<Member(%s %s)>" % (self.id, self.name)

    def to_dictionary(self):
        return dict(id=self.id, conv_user=self.conv_user, content=self.content)
