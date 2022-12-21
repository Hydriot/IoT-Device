from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager
from src.data_access.database.common.sqllite_database import SQLLiteDatabase
from src.infrastructure.config.config_manager import ConfigManager

logger = LogManager().logger
database = SQLLiteDatabase()

class PhSchedule(SchedulingBase):

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__)

    def exec(self):

        try:
          logger.info("Tic")

        except Exception as ex:
            logger.error(f"Oops! {ex.__class__} occurred. Details: {ex}")
