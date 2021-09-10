from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class Country(TimeBaseModel):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)
    cities = relationship("City", back_populates="country")
