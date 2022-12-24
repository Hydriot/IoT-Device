from src.application.sensors.sensor_base import SensorBase
from src.common.sensor_type import SensorType

class WaterLevelSensor(SensorBase):

    def __init__(self) -> None:
        super().__init__(SensorType.WaterLevelSensor)

    def _read_raw_value(self):
        raise ValueError("Not implimented exception - Water Level Sensor")