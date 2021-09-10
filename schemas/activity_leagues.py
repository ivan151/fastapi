from sqlalchemy import Integer, Column, String, sql, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class ActivityLeague(TimeBaseModel):
    __tablename__ = 'activity_leagues'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    cover_id = Column(Integer, ForeignKey('covers.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_type_id = Column(Integer, ForeignKey("activity_types.id", ondelete="RESTRICT", onupdate="CASCADE"))
    activity_format_id = Column(Integer, ForeignKey('activity_formats.id', ondelete='RESTRICT', onupdate='CASCADE'))

    activity = relationship("Activity", back_populates="leagues")
    format = relationship("ActivityFormat", back_populates="leagues")
    type = relationship("ActivityType", back_populates="leagues")
    team_profiles = relationship("TeamProfile", back_populates="league")
    team_requests = relationship("TeamRequest", back_populates="league")