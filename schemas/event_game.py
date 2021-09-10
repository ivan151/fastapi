from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class EventGame(TimeBaseModel):
    __tablename__ = 'event_games'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('events.id', ondelete="CASCADE", onupdate="CASCADE"))
    referee_user_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    home_team_id = Column(Integer, ForeignKey('teams.id', ondelete="CASCADE", onupdate="CASCADE"))
    guest_team_id = Column(Integer, ForeignKey('teams.id', ondelete="CASCADE", onupdate="CASCADE"))
    home_score = Column(Integer)
    visitor_score = Column(Integer)
    info = Column(String(500))

    event = relationship("Event", back_populates="games")
    referee = relationship("User", back_populates="games")
