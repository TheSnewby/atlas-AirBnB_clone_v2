#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import storage_type


class Review(BaseModel, Base):
    __tablename__ = 'reviews'

    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

        place = relationship("Place", backref="reviews", cascade="all, delete-orphan")
        user = relationship("User", backref="reviews", cascade="all, delete-orphan")

    else:
        text = ''
        place_id = ''
        user_id = ''
