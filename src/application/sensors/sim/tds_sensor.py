from src.application.sensors.sensor_base import SensorBase
from src.infrastructure.logger import LogManager

import random
logger = LogManager().logger

class TdsSensorSim(SensorBase):
    previous_value = None
   

    def _read_raw_value(self):
        new_value = None
    
        if (self.previous_value == None):
            new_value = random.randrange(300,800)
            
        else:
            rand = random.randrange(1,4) # Create artificial stability in the simulated value

            if (rand == 1):
                movement = random.randrange(-50,50)

                new_value = self.previous_value + movement
            else:
                new_value = self.previous_value

        self.previous_value = new_value
        return new_value     
       
