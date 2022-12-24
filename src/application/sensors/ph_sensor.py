from src.application.sensors.sensor_base import SensorBase

class PhSensor(SensorBase):

    def _read_raw_value(self):
        raise ValueError("Not implimented exception - WaterLevelSensor")