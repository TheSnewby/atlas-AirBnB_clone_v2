#!/usr/bin/python3
"""This module defines a class Place"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
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
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)

        # Relationships
        user = relationship("User", back_populates="places")
        city = relationship("City", back_populates="places")
            # cascade="all, delete-orphan"
    else:
        user_id = ''
        city_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
