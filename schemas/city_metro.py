from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from schemas.field_city_metro import field_metro
from schemas.base import TimeBaseModel


class CityMetro(TimeBaseModel):
    __tablename__ = 'city_metro'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete="CASCADE", onupdate="CASCADE"))

    city = relationship("City", back_populates="stations")
    fields = relationship('Field', secondary=field_metro,
                          back_populates='stations', lazy='dynamic')
