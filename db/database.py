"""
Provides access to main database accessors, engine, etc.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config import EnvConfig

env = EnvConfig()


class Database:
    """
    Database boiler-plate management class
    """

    engine = create_engine(env.database_url, echo=env.debug_database)
    Base = declarative_base()
    db_initialised = False

    def __init__(self):
        """
        Initialise properties
        """
        self.Session = None

    @staticmethod
    def init_db():
        """
        Initialise database tables
        """
        if not Database.db_initialised:
            Database.Base.metadata.create_all(Database.engine)
            Database.db_initialised = True

    def get_session(self):
        """
        Returns a new session, sessions should be closed after usage, usually in a Finally block.
        """
        if not self.Session:
            self.Session = scoped_session(sessionmaker(bind=Database.engine))
        return self.Session()

