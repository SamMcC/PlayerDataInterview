"""
Provides UserInfo class for the ORM model
"""

from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship

from db.database import Database


class UserInfo(Database.Base):
    """
    Defines a user as a name and a weight
    """
    __tablename__ = 'user_data'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='name')
    weight_kg = Column(Float, name='weight_kg')
    runs = relationship('RunInfo', back_populates='user')
