from typing import List
from sqlalchemy import Column, DateTime, func, Table, inspect

from database import Base


class BaseModel(Base):
    __abstract__ = True

    def __str__(self):
        model = self.__class__.__name__
        table: Table = inspect(self.__class__)
        primary_key_columns: List[Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"


class TimeBaseModel(BaseModel):
    __abstract__ = True

    created_at = Column(DateTime(True), server_default=func.now())
    updated_at = Column(DateTime(True),
                        default=func.now(),
                        onupdate=func.now(),
                        server_default=func.now())
