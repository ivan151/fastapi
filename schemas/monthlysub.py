import datetime

from sqlalchemy import Integer, Column, String, sql
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


from schemas.base import TimeBaseModel


class MonthlySub(TimeBaseModel):
    __tablename__ = 'monthly_sub'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    sub_name = Column(String(200))
    price = Column(Integer)
    month = Column(Integer, default=None)
    year = Column(Integer, default=datetime.datetime.now().year)

    creator = relationship("User", back_populates="subs")


# async def main():
#     await db.gino.create_all()
#
# asyncio.get_event_loop().run_until_complete(main())