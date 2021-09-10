from sqlalchemy import Integer, Column, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class EventTeam(TimeBaseModel):
    __tablename__ = 'event_teams'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id', ondelete="CASCADE", onupdate="CASCADE"))
    event_id = Column(Integer, ForeignKey('events.id', ondelete="CASCADE", onupdate="CASCADE"))
    price = Column(Integer, default=0)
    price_calc_type = Column('price_calc_type', ENUM(name='price_calc_type'))
    price_per_user = Column(Integer, default=0)
    participants_min = Column(Integer)
    participants_max = Column(Integer)
    info = Column(String(500), default=None)

    event = relationship("Event", back_populates="teams")
    team = relationship("Team", back_populates="events")