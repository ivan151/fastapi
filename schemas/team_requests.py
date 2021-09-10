from sqlalchemy import Integer, Column, BigInteger, String, sql, Boolean
from sqlalchemy.dialects.postgresql import INT4RANGE
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class TeamRequest(TimeBaseModel):
    __tablename__ = 'team_requests'
    id = Column(BigInteger, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_role = Column(Integer, ForeignKey('activity_roles.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_format = Column(Integer, ForeignKey('activity_formats.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_league_id = Column(Integer, ForeignKey('activity_leagues.id', ondelete='RESTRICT', onupdate='CASCADE'))
    team_profile_id = Column(Integer, ForeignKey('team_profiles.id', ondelete="CASCADE", onupdate="CASCADE"))
    age = Column(INT4RANGE, nullable=False)
    description = Column(String(500))
    is_active = Column(Boolean, default=True)

    activity = relationship("Activity", back_populates="team_requests")
    format = relationship("ActivityFormat", back_populates="team_requests")
    league = relationship("ActivityLeague", back_populates="team_requests")
    team_profile = relationship("TeamProfile", back_populates="team_requests")



    query: sql.Select