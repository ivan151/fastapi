from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey, MetaData, Table

from database import metadata, Base

field_metro = Table('field_metro', Base.metadata,
                    Column('field_id', ForeignKey('fields.id')),
                    Column('metro_id', ForeignKey('city_metro.id'))
                    )

