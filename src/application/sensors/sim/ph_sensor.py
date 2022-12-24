from src.application.sensors.sensor_base import SensorBase
from src.infrastructure.logger import LogManager

import random
logger = LogManager().logger

class PhSensorSim(SensorBase):
    previous_value = None
   

    def _read_raw_value(self):
        new_value = None
    
        if (self.previous_value == None):
            new_value = random.randrange(500,800)
            
        else:
            rand = random.randrange(1,4) # Create artificial stability in the simulated value

            if (rand == 1):
                movement = random.randrange(-1,1)

                new_value = self.previous_value + movement

                if (new_value < 0):
                    new_value = 0
                
                if (new_value > 7):
                    new_value = 7
            else:
                new_value = self.previous_value

        self.previous_value = new_value
        return new_value     
       
