# Database Manager
from sql.database.database_manager import DatabaseManager

database_manager = DatabaseManager.sharedInstance()
Base = database_manager.Base
from sql.database.context_manager import session

# Create Tables
from sql.orm_models import *

Base.metadata.create_all(bind=database_manager.engine)
from commons.load_config import load_configuration

config = load_configuration()
