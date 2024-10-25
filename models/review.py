#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine import storage_type

class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    if storage_type == 'db':
        place_id = Column(String(60))  # PLACEHOLDER PARAMETERS
        user_id = Column(String(60))  # PLACEHOLDER PARAMETERS
        text = Column(String(60))  # PLACEHOLDER PARAMETERS
    else:
        place_id = ""
        user_id = ""
        text = ""
