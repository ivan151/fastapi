from sqlalchemy import Integer, Column, String, sql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel


class District(TimeBaseModel):
    __tablename__ = 'city_districts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"))

    city = relationship("City", back_populates="districts")
    fields = relationship("Field", back_populates="district")

    query: sql.Select
