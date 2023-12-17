#!/usr/bin/python3
"""
Only one class State
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines model State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete-orphan")

