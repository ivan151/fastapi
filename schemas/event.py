from sqlalchemy import Integer, Column, DateTime, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class Event(TimeBaseModel):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    description = Column(String(500))
    address = Column(String(100))
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_contest_id = Column(Integer, ForeignKey('activity_contests.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_format_id = Column(Integer, ForeignKey('activity_formats.id', ondelete='RESTRICT', onupdate='CASCADE'))
    cover_id = Column(Integer, ForeignKey('covers.id', ondelete='RESTRICT', onupdate='CASCADE'))
    creator_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    type_id = Column(Integer, ForeignKey('activity_types.id', ondelete="RESTRICT", onupdate="CASCADE"))
    field_id = Column(Integer, ForeignKey('fields.id', ondelete="RESTRICT", onupdate="CASCADE"))

    games = relationship("EventGame", back_populates="event")
    teams = relationship("EventTeam", back_populates="event")
    activity = relationship("Activity", back_populates="events")
    type = relationship("ActivityType", back_populates="events")
    format = relationship("ActivityFormat", back_populates="events")
    cover = relationship("Cover", back_populates="events")
    creator = relationship("User", back_populates="events")
    field = relationship("Field", back_populates="events")
