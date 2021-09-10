from sqlalchemy import Integer, Column, String, sql, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class UserProfile(TimeBaseModel):
    __tablename__ = 'user_profiles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete="CASCADE", onupdate="CASCADE"))
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_role_id = Column(Integer, ForeignKey('activity_roles.id', ondelete='RESTRICT', onupdate='CASCADE'))
    is_looking = Column(Boolean, default=False)
    experience = Column(String(10000), default=None)

    user = relationship("User", back_populates="profiles")
    activity = relationship("Activity", back_populates="user_profiles")
    role = relationship("ActivityRole", back_populates="user_profiles")
