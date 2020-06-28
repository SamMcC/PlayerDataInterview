from sqlalchemy import Column, String, Integer, Float

from db.database import Base


class UserInfo(Base):
    __tablename__ = 'runs'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='name')
    weight_kg = Column(Float, name='weight_kg')
