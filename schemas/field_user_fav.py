from sqlalchemy import Column
from sqlalchemy.sql.schema import ForeignKey, MetaData, Table

from database import metadata, Base
from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from schemas.base import TimeBaseModel
from schemas.field_city_metro import field_metro
from schemas.field_activity import field_activity

field_user_fav = Table('field_user_fav', Base.metadata,
                       Column('field_id', ForeignKey('fields.id')),
                       Column('user_id', ForeignKey('users.id'))
                       )
