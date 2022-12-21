import json
import traceback
from pathlib import Path

from src.common.runtime_details import RunTimeDetails
from src.infrastructure.config.schema import Schema
from src.infrastructure.logger import LogManager

logger = LogManager().logger

class ConfigManager:
    _global_configuration_filename = "app_config.json"
    runtime_details: RunTimeDetails = None
    settings: Schema = None

    @staticmethod
    def _read_config_file(path: Path) -> dict:
        try:
            with open(path, 'r') as file:
                data: dict = json.load(file)
            return data
        except Exception:
            logger.error(
                f"""
                Failed to read configurations settings for [{path}]. 
                See the stack trace bellow for details. >>>>>>>>>>>>
                >> {traceback.format_exc()}
                """
            )
            raise

    def _load_configuration(self) -> Schema:
        data = self._read_config_file(self.global_config_path)
        return Schema.parse_obj(data)


    def __init__(self) -> None:
        self.runtime_details = RunTimeDetails()
        self.settings: Schema = self._load_configuration()


    @property
    def global_config_path(self) -> Path:
        config_filename = self.__class__._global_configuration_filename
        root_dir = self.runtime_details.get_root_directory()
        file_path = f"{root_dir}/{config_filename}"

        return file_path




