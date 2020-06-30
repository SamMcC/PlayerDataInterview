"""
Provides RunInfo class for the ORM model
"""
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Database


class RunInfo(Database.Base):
    """
    Represents a single run in the database
    """
    __tablename__ = 'run_data'

    id = Column(Integer, primary_key=True)
    time_h = Column(Float, name='time_h')
    distance_km = Column(Float, name='distance_km')
    date = Column(DateTime, name='date')
    user_id = Column(Integer, ForeignKey('user_data.id'), name='user_id')
    user = relationship('UserInfo', back_populates='runs')
