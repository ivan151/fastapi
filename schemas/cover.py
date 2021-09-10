from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel


class Cover(TimeBaseModel):
    __tablename__ = 'covers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), default=None)

    events = relationship("Event", back_populates="cover")
    fields = relationship("Field", back_populates="cover")