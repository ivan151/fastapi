from sqlalchemy import Column, BigInteger, String, Integer, Boolean
from sqlalchemy import Date
from sqlalchemy.future import select
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from schemas.field_user_fav import field_user_fav
from schemas.base import TimeBaseModel


class User(TimeBaseModel):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger)
    name = Column(String(100))
    login = Column(String(100), default=None)
    password_hash = Column(String, default=None)
    phone_number = Column(BigInteger)
    photo_file_id = Column(Integer, ForeignKey('files.id', ondelete="RESTRICT", onupdate="CASCADE"))
    is_admin = Column(Boolean, default=False)
    is_referee = Column(Boolean, default=False)
    is_organizer = Column(Boolean, default=False)
    is_bot = Column(Boolean, default=False)
    gender = Column(Boolean, default=None)
    birth_date = Column(Date)
    city_id = Column(Integer, ForeignKey('cities.id', ondelete="RESTRICT", onupdate="CASCADE"))
    district_id = Column(Integer, ForeignKey('city_districts.id', ondelete="CASCADE", onupdate="CASCADE"))
    game_balance = Column(Integer, default=0)

    events = relationship("Event", back_populates="creator")
    games = relationship("EventGame", back_populates="referee")
    fields = relationship("Field", back_populates="creator")
    fav_fields = relationship('Field', secondary=field_user_fav,
                              back_populates='users', lazy='dynamic')
    fund_raises = relationship("FundRaise", back_populates="creator")
    subs = relationship("MonthlySub", back_populates="creator")
    team_profiles = relationship("TeamProfileUser", back_populates="user")
    teams = relationship("TeamUser", back_populates="user")
    profiles = relationship("UserProfile", back_populates="user")

    @classmethod
    async def get_user(cls, db_session: sessionmaker, id: int) -> 'User':
        async with db_session() as db_session:
            sql = select(cls).where(cls.id == id)
            request = await db_session.execute(sql)
            user: cls = request.scalar()
        return user

