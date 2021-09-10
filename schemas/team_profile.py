from sqlalchemy import Integer, Column, BigInteger, String, sql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class TeamProfile(TimeBaseModel):
    __tablename__ = 'team_profiles'
    id = Column(Integer, primary_key=True)
    team_id = Column(BigInteger, ForeignKey('teams.id', ondelete="CASCADE"))
    activity_id = Column(Integer, ForeignKey('activities.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_league_id = Column(Integer, ForeignKey('activity_leagues.id', ondelete="RESTRICT", onupdate="CASCADE"))
    activity_contest_id = Column(Integer, ForeignKey('activity_contests.id', ondelete='RESTRICT', onupdate='CASCADE'))
    activity_format_id = Column(Integer, ForeignKey('activity_formats.id', ondelete='RESTRICT', onupdate='CASCADE'))
    description = Column(String(2000), default=None)

    team = relationship("Team", back_populates="profiles")
    activity = relationship("Activity", back_populates="team_profiles")
    league = relationship("ActivityLeague", back_populates="team_profiles")
    contest = relationship("ActivityContest", back_populates="team_profiles")
    format = relationship("ActivityFormat", back_populates="team_profiles")
    users = relationship("TeamProfileUser", back_populates="team_profile")
    team_requests = relationship("TeamRequest", back_populates="team_profile")