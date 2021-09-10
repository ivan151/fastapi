from sqlalchemy import Column, BigInteger, String, sql, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class Team(TimeBaseModel):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    cap_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    city_id = Column(Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"))
    city_district_id = Column(Integer, ForeignKey('city_districts.id', ondelete="CASCADE", onupdate="CASCADE"))
    tg_channel_id = Column(BigInteger)
    key = Column(String(100))
    photo_id = Column(String(100), default=None)

    profiles = relationship('TeamProfile', back_populates='team')
    events = relationship("EventTeam", back_populates="team")
    users = relationship("TeamUser", back_populates="team")
