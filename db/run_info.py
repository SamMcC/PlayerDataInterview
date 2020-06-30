"""
Provides RunInfo class for the ORM model
"""
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey

from db.database import Database
from db.user_info import UserInfo


class RunInfo(Database.Base):
    """
    Represents a single run in the database
    """
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    time_h = Column(Float, name='time_h')
    distance_km = Column(Float, name='distance_km')
    date = Column(DateTime, name='date')
    user_id = ForeignKey(UserInfo.id, name='user_id')
