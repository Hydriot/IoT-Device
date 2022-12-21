##from doctest import master

from src.data_access.database.models import database_models
from src.infrastructure.thread_manager import ThreadManager, ThreadType
from src.distribution.schedules.scheduler import Scheduler
from src.data_access.database.common.sqllite_database import SQLLiteDatabase
from threading import Thread
from src.infrastructure.logger import LogManager

logger = LogManager().logger
database = SQLLiteDatabase()

def main():

    database_models.Base.metadata.create_all(database.engine) # Create/Sync database   

    thread_manager = ThreadManager()
    
    # Start Scheduler on its own thread
    scheduler = Scheduler()
    scheduler_thread = Thread(target=scheduler.start,args=(thread_manager,))    
    thread_manager.add_update_thread(thread_type=ThreadType.Scheduler, thread=scheduler_thread)
    scheduler_thread.start()

main()