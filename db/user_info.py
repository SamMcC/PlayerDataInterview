"""
Provides UserInfo class for the ORM model
"""

from sqlalchemy import Column, String, Integer, Float

from db.database import Database


class UserInfo(Database.Base):
    """
    Defines a user as a name and a weight
    """
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='name')
    weight_kg = Column(Float, name='weight_kg')
    height_m = Column(Float, name='height_m')
