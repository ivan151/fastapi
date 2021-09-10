from sqlalchemy import Integer, Column, String, sql, ForeignKey
from sqlalchemy.orm import relationship
from schemas.base import TimeBaseModel

class ActivityRole(TimeBaseModel):
    __tablename__ = 'activity_roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))

    activity = relationship("Activity", back_populates="roles")
    user_profiles = relationship("UserProfile", back_populates="role")