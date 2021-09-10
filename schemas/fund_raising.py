from sqlalchemy import Integer, Column, String, sql, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


from schemas.base import TimeBaseModel

class FundRaise(TimeBaseModel):
    __tablename__ = 'fundraise'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('users.id', ondelete="RESTRICT", onupdate="CASCADE"))
    point = Column(String(100))
    date = Column(Date)
    amount = Column(Integer)

    creator = relationship("User", back_populates="fund_raises")