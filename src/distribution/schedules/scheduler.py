import asyncio

from src.distribution.schedules.common.schedule_manager import ScheduleManager
from src.distribution.schedules.common.overview_schedule import OverviewSchedule
from src.infrastructure.config.config_manager import ConfigManager

from src.distribution.schedules.water_level_schedule import WaterLevelSchedule
from src.distribution.schedules.tds_schedule import TdsSchedule
from src.distribution.schedules.ph_schedule import PhSchedule

class Scheduler():
    schedule_manager = ScheduleManager()
    thread_manager = None
    config = ConfigManager().settings

    water_level_schedule = WaterLevelSchedule()
    tds_schedule = TdsSchedule()
    ph_schedule = PhSchedule()

    overview = OverviewSchedule()

    async def register_schedules(self):
        asyncio.ensure_future(self.water_level_schedule.start(self.schedule_manager, self.config.sensors.water_level_sensor.frequency_in_seconds))
        asyncio.ensure_future(self.tds_schedule.start(self.schedule_manager, self.config.sensors.tds_sensor.frequency_in_seconds))
        asyncio.ensure_future(self.ph_schedule.start(self.schedule_manager, self.config.sensors.ph_sensor.frequency_in_seconds))

        asyncio.ensure_future(self.overview.start(self.schedule_manager, 5))

    def start(self, thread_manager):
        self.thread_manager = thread_manager
        
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        try:
            asyncio.ensure_future(self.register_schedules())
            loop.run_forever()
        finally:
            loop.close()
