from sqlalchemy.sql.schema import ForeignKey, Table, Column

from database import metadata, Base

field_activity = Table('field_activity', Base.metadata,
                       Column('field_id', ForeignKey('fields.id')),
                       Column('activity_id', ForeignKey('activities.id'))
                       )

