from typing import Optional
from pydantic import BaseModel

class DatabaseDetails(BaseModel):
    serverName: Optional[str]
    databaseName: Optional[str]
    databaseUser: Optional[str]
    databaseUserPassword: Optional[str]

class Databases(BaseModel):
    main: DatabaseDetails = DatabaseDetails()

# The ROOT Configuration class
class Schema(BaseModel):
    databases: Databases






