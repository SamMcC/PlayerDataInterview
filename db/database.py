"""
Provides access to main database accessors, engine, etc.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from config import EnvConfig

env = EnvConfig()

ENGINE = create_engine(env.database_url, echo=env.debug_database)
Base = declarative_base()
