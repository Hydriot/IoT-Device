from src.data_access.database.common.database_base import DatabaseBase
from sqlalchemy import create_engine

class SQLLiteDatabase(DatabaseBase):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./hydriot_local.db"

    def _create_engine(self):
        engine = create_engine(
                self.SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
            )
        
        return engine