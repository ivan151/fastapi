from sqlalchemy import Integer, Column, Boolean, String
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class EventParticipant(TimeBaseModel):
    __tablename__ = 'event_participants'
    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id', ondelete="CASCADE", onupdate="CASCADE"))
    event_id = Column(Integer, ForeignKey('events.id', ondelete="CASCADE", onupdate="CASCADE"))
    user_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    name = Column(String(100))
    state = Column('state', ENUM(name='state'), default=None)
    is_paid = Column(Boolean, default=False)
