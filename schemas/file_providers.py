from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy.orm import relationship
from sqlalchemy.types import JSON
from sqlalchemy import Integer, Column, sql

from schemas.base import TimeBaseModel


class FileProvider(TimeBaseModel):
    __tablename__ = 'file_providers'
    id = Column(Integer, primary_key=True)
    type = Column('type', ENUM(name='file_providers_type'))
    options = Column(JSON)

    files = relationship("File", back_populates="provider")
