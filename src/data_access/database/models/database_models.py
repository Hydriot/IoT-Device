from ast import Index
from datetime import datetime
from tokenize import String
from unicodedata import name
from src.data_access.database.common.database import Base
from sqlalchemy.sql import null
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Column, UniqueConstraint

class SensorEntity(Base):
    __tablename__ = 'Sensors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    requires_sync = Column(Boolean)
    client_account = Column(String)
    device_reference = Column(String)

    def create(self, name, type, client_account, device_reference, id = None):
        self.id = id
        self.name = name
        self.type = type
        self.requires_sync = False
        self.client_account = client_account
        self.device_reference = device_reference

        return self


class SensorValueEntity(Base):
    __tablename__ = 'SensorValues'
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)

    from_date = Column(DateTime)
    to_date = Column(DateTime)
    last_updated = Column(DateTime)
    is_placeholder = Column(Boolean)
       
    # Foreign Key - One Side Oposed to Many
    sensor_id = Column(Integer, ForeignKey('Sensors.id'))

    def create(self, value, from_date, to_date, is_placeholder = False, id = None):
        self.id = id
        self.value = value
        self.from_date = from_date
        self.to_date = to_date
        self.last_updated = datetime.now()
        self.is_placeholder = is_placeholder

        return self