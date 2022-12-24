import os

from src.distribution.schedules.common.schedule_base import SchedulingBase
from src.infrastructure.logger import LogManager
from src.infrastructure.config.config_manager import ConfigManager

logger = LogManager().logger

class OverviewSchedule(SchedulingBase):

    logger = LogManager().logger
    toggle = False
    config = None

    def do_toggle(self, bit) -> bool:
        if bit == True:
            bit = False
        else:
            bit = True        
        return bit

    def __init__(self):
        SchedulingBase.__init__(self, type(self).__name__)
        self.config = ConfigManager().settings

    def exec(self):
        self.toggle = self.do_toggle(self.toggle)
        token = "+" if self.toggle else "-"

        os.system("clear")
        print()
        print("=====================================================")
        print(f"{token} =============  Running Schedules ================ {token}")
        print("=====================================================")
        print("")

        if (self.config.simulator_enabled):
            print("!Warning! Simulator enabled, these are not real values.")
            print("")

        for schedule_key in self.schedule_manager.schedules:
            # Ignore the overview schedule
            if schedule_key == type(self).__name__:
                continue

            schedule = self.schedule_manager.schedules[schedule_key]
            last_run = "N/A" if schedule.stopwatch.last_success_time is None else schedule.stopwatch.last_success_time.strftime("%Y-%m-%d %H:%M:%S")
            last_duration = "N/A" if schedule.stopwatch.last_success_time is None else str(round(schedule.stopwatch.elapsed_time_in_seconds(), 2))
            current_value = "N/A" if schedule.sensor.current_value is None else str(schedule.sensor.current_value)

            logger.info(f"[{schedule.name}]: Active, last ran at {last_run} for {last_duration}s current value >> [{current_value}]")
        print()

        