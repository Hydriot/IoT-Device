from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager
from src.data_access.database.common.sqllite_database import SQLLiteDatabase
from src.application.sensors.sensor_base import SensorBase
from src.infrastructure.config.config_manager import ConfigManager
import time

from src.application.sensors.sim.tds_sensor import TdsSensorSim
from src.application.sensors.tds_sensor import TdsSensor

logger = LogManager().logger
database = SQLLiteDatabase()

class TdsSchedule(SchedulingBase):
    sensor:SensorBase = None
    is_simulated = False

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__)
        self.is_simulated = ConfigManager().settings.simulator_enabled

        if (self.is_simulated):
            self.sensor = TdsSensorSim()
        else:
            self.sensor = TdsSensor()

    def exec(self):

        try:
          value = self.sensor.read_value()
          #TODO: update SCD

          if (self.is_simulated):
            time.sleep(1)

        except Exception as ex:
            logger.error(f"Oops! {ex.__class__.__name__} occurred. Details: {ex}")