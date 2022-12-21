from datetime import datetime
from abc import ABC, abstractmethod
from src.infrastructure.logger import LogManager

logger = LogManager().logger

class SensorBase(ABC):    
    last_read_time: datetime = None

    # override this method if a conversion must take place
    def convert_raw(self, raw_value):
        return raw_value

    @abstractmethod
    def _read_raw_value(self):
        pass

    def read_value(self):
        try:
            raw_value = self._read_raw_value()
            converted = self.convert_raw(raw_value)
            self.last_read_time = datetime.now()
            
            return converted

        except Exception as ex:
            logger.error(f"Oops! {ex.__class__} occurred. Details: {ex}")  

        raise # re-throw after writing error to screen
        
