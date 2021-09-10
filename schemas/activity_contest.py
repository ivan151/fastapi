from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class ActivityContest(TimeBaseModel):
    __tablename__ = 'activity_contests'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    activity_league_id = Column(Integer, ForeignKey('activity_leagues.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    cover_id = Column(Integer, ForeignKey('covers.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_format_id = Column(Integer, ForeignKey('activity_formats.id', ondelete='RESTRICT', onupdate='CASCADE'))
    date_start = Column(DateTime)
    date_end = Column(DateTime)

    activity = relationship("Activity", back_populates="contests")
    format = relationship("ActivityFormat", back_populates="contests")
    team_profiles = relationship("TeamProfile", back_populates="contest")