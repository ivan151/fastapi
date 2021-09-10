from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel
from schemas.field_city_metro import field_metro
from schemas.field_user_fav import field_user_fav
from schemas.field_activity import field_activity


class Field(TimeBaseModel):
    __tablename__ = 'fields'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    name = Column(String(100))
    address = Column(String(100))
    photo_file_id = Column(Integer, ForeignKey('files.id', ondelete="RESTRICT", onupdate="CASCADE"))
    url = Column(String(1000), default=None)
    price = Column(Integer, default=0)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete="RESTRICT", onupdate="CASCADE"))
    district_id = Column(Integer, ForeignKey('city_districts.id', ondelete="RESTRICT", onupdate="CASCADE"))
    cover_id = Column(Integer, ForeignKey('covers.id', ondelete='RESTRICT', onupdate='CASCADE'))
    fs_id = Column(Integer)
    metro_id = Column(Integer, ForeignKey('city_metro.id', ondelete="CASCADE", onupdate="CASCADE"))

    creator = relationship("User", back_populates="fields")
    events = relationship("Event", back_populates="field")
    city = relationship("City", back_populates="fields")
    district = relationship("District", back_populates="fields")
    cover = relationship("Cover", back_populates="fields")
    activities = relationship('Activity', secondary=field_activity,
                              back_populates='fields', lazy='dynamic')
    stations = relationship('CityMetro', secondary=field_metro,
                            back_populates='fields', lazy='dynamic')
    users = relationship("User", secondary=field_user_fav,
                         back_populates="fav_fields", lazy='dynamic')

# async def main():
#     await db.gino.create_all()
#
#
# asyncio.get_event_loop().run_until_complete(main())
