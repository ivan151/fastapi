from sqlalchemy import Integer, Column, String, sql, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class ActivityFormat(TimeBaseModel):
    __tablename__ = 'activity_formats'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))

    activity = relationship("Activity", back_populates="formats")
    team_profiles = relationship("TeamProfile", back_populates="format")
    leagues = relationship("ActivityLeague", back_populates="format")
    team_requests = relationship("TeamRequest", back_populates="format")
    contests = relationship("ActivityContest", back_populates="format")
    events = relationship("Event", back_populates="format")