from typing import Optional
from pydantic import BaseModel

class Sensor(BaseModel):
    enabled: Optional[bool]
    decimal_places: Optional[int]
    frequency_in_seconds: Optional[int]

class Sensors(BaseModel):
    water_level_sensor: Optional[Sensor]
    tds_sensor: Optional[Sensor]
    ph_sensor: Optional[Sensor]

class Integration(BaseModel):
    endpoint: Optional[str]
    api_key: Optional[str]

# The ROOT Configuration class
class Schema(BaseModel):
    simulator_enabled: bool
    sensors: Sensors
    integration: Integration







