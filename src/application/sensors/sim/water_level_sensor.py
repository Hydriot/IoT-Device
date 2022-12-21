from src.application.sensors.sensor_base import SensorBase
from src.infrastructure.logger import LogManager

import random
logger = LogManager().logger

class WaterLevelSensorSim(SensorBase):
    previous_value = None

    def toggle(self, value):
        if value == 1:
            return 0
        else:
            return 1

    def convert_raw(self, raw_value):
        if raw_value == None:
            return None

        if raw_value == 1:
            return True
        elif raw_value == 0:
            return False
        else:
            raise ValueError(f"Unexpected result [{raw_value}] returned from reading, expected 1 or 0.")

    def _read_raw_value(self):
        new_value = None
    
        if (self.previous_value == None):
            new_value = random.randrange(0,1)
            logger.info(f"New >>> rand [{new_value}]")
        else:
            rand = random.randrange(1,5) # Create artificial stability in the simulated value

            if (rand == 1):
                new_value = self.toggle(self.previous_value)
            else:
                new_value = self.previous_value

        self.previous_value = new_value
        return new_value     
       
