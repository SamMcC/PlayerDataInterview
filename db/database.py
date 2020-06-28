from sqlalchemy import create_engine
from config import EnvConfig
from sqlalchemy.ext.declarative import declarative_base

env = EnvConfig()

ENGINE = create_engine(env.database_url, echo=env.debug_database)
Base = declarative_base()
