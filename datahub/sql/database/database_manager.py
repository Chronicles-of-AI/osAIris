from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData, create_engine, DDL, event
import os

# from sql import logger

# logging = logger(__name__)


class DatabaseManager:

    __instance = None

    def __setup_schema(self):
        event.listen(
            self.Base.metadata,
            "before_create",
            DDL("CREATE SCHEMA IF NOT EXISTS osairis_schema"),
        )

    @staticmethod
    def sharedInstance():
        """Static access method."""
        if DatabaseManager.__instance is None:
            DatabaseManager()
        return DatabaseManager.__instance

    def __init__(self):
        """Virtually private constructor."""
        if DatabaseManager.__instance is not None:
            try:
                raise Exception("Instance exists!")
            except Exception as e:
                print(e)
                # logging.error(e)
        else:
            postgres_url = os.environ.get("db_url")
            self.db_url = f"postgresql://postgres:postgres@{postgres_url}/postgres"
            # logging.info(f"Database Url: {self.db_url}")
            self.metadata = MetaData(schema="osairis_schema")
            self.engine = create_engine(self.db_url, pool_pre_ping=True)
            self.Base = declarative_base(metadata=self.metadata)
            self.SessionMaker = sessionmaker(bind=self.engine)
            self.__setup_schema()
            DatabaseManager.__instance = self
