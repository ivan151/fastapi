from sqlalchemy import Integer, Column, sql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class TeamProfileUser(TimeBaseModel):
    __tablename__ = 'team_profile_users'
    id = Column(Integer, primary_key=True)
    team_profile_id = Column(Integer, ForeignKey('team_profiles.id', ondelete="CASCADE", onupdate="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    number = Column(Integer)
    team_profile = relationship("TeamProfile", back_populates="users")
    user = relationship("User", back_populates="team_profiles")
