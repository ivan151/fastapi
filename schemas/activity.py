from sqlalchemy import Integer, Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from schemas import field_activity
from schemas.base import TimeBaseModel


class Activity(TimeBaseModel):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    fs_id = Column(Integer)
    is_sport = Column(Boolean, default=True)
    country_id = Column(Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"))

    events = relationship("Event", back_populates="activity")
    contests = relationship("ActivityContest", back_populates="activity")
    roles = relationship("ActivityRole", back_populates="activity")
    formats = relationship("ActivityFormat", back_populates="activity")
    types = relationship("ActivityType", back_populates="activity")
    leagues = relationship("ActivityLeague", back_populates="activity")
    fields = relationship('Field', secondary=field_activity, back_populates='activities', lazy='dynamic')
    team_profiles = relationship("TeamProfile", back_populates="activity")
    team_requests = relationship("TeamRequest", back_populates="activity")
    user_profiles = relationship("UserProfile", back_populates="activity")
