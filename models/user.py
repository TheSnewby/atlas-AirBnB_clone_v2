#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base  # Ensure this line is correct
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    # Class attributes representing columns
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    
    # Relationship with Place (if applicable)
    places = relationship("Place", back_populates="user", cascade="all, delete-orphan")
