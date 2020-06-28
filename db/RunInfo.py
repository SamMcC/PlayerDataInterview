from sqlalchemy import Column, Integer, Float, DateTime

from db.database import Base


class RunInfo(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    time_h = Column(Float, name='time_h')
    distance_km = Column(Float, name='distance_km')
    date = Column(DateTime, name='date')
