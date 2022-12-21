from datetime import datetime
from doctest import master

from src.data_access.database.common.database import get_db_Session, engine
from src.data_access.database.models import database_models
from src.infrastructure.logger import LogManager

logger = LogManager().logger

def main():
    database_models.Base.metadata.create_all(engine) # Create/Sync database

    logger.info("Hydriot IoT Device Starting...")

    ##TODO: Register Scedules
    ##TODO: Register Website

main()