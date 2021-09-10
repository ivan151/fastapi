from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class City(TimeBaseModel):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    country_id = Column(Integer, ForeignKey('countries.id', ondelete="CASCADE", onupdate="CASCADE"))

    districts = relationship("District", back_populates="city")
    stations = relationship("CityMetro", back_populates="city")
    country = relationship("Country", back_populates="cities")
    fields = relationship("Field", back_populates="city")



