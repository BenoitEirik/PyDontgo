from sqlalchemy import Column, String, UniqueConstraint, Integer, ForeignKey
from API.model.mapping import Base


class ConvUser(Base):
    __tablename__ = 'conv_user'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    conv_id = Column(Integer, ForeignKey('conversation.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    nickname = Column(String(20))

    def __repr__(self):
        return "<Member(%s %s)>" % (self.id, self.name)

    def to_dictionary(self):
        return dict(user_id=self.user_id, conv_id=self.conv_id, role_id=self.role_id, nickname=self.nickname)
