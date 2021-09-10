from sqlalchemy import Integer, Column, sql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class TeamUser(TimeBaseModel):
    __tablename__ = 'team_users'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id', ondelete="CASCADE", onupdate="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    balance = Column(Integer, default=0)

    team = relationship("Team", back_populates="users")
    user = relationship("User", back_populates="teams")
