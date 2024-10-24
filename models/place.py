#!/usr/bin/python3
"""This module defines a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import storage_type


class Place(BaseModel, Base):
    """This class defines a place by various attributes"""
    __tablename__ = 'places'
    if storage_type == 'db':
        # Class attributes representing columns
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        name = Column(String(128), nullable=False)

        # Relationships
        user = relationship("User", back_populates="places")
        city = relationship(
            "City",
            back_populates="places")
            # cascade="all, delete-orphan"
    else:
        user_id = ''
        city_id = ''
        name = ''
