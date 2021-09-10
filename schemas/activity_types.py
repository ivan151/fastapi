from sqlalchemy import Integer, Column, String, sql, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class ActivityType(TimeBaseModel):
    __tablename__ = 'activity_types'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))

    activity = relationship("Activity", back_populates="types")
    events = relationship("Event", back_populates="type")
    leagues = relationship("ActivityLeague", back_populates="type")

