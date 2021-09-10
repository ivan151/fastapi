from sqlalchemy import Integer, Column, sql, ForeignKey, String
from sqlalchemy.orm import relationship

from schemas.base import TimeBaseModel

class File(TimeBaseModel):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey('file_providers.id',
                                             ondelete="RESTRICT", onupdate="CASCADE"))
    key = Column(String, nullable=False)

    provider = relationship("FileProvider", back_populates="files")
