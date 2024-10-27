#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""

from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime


class BaseModel:
    """Base class for all models in the AirBnB clone."""

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiate a new model."""
        if not kwargs:
            self.id = str(uuid.uuid4())
            current_time = datetime.utcnow()
            self.created_at = current_time
            self.updated_at = current_time
        else:
            self.id = kwargs.get('id', str(uuid.uuid4()))
            self.created_at = self.parse_datetime(kwargs.get('created_at', datetime.utcnow()))
            self.updated_at = self.parse_datetime(kwargs.get('updated_at', datetime.utcnow()))

            # Clean up unwanted keys
            kwargs.pop('__class__', None)

            # Set attributes from kwargs, excluding special keys
            for key, val in kwargs.items():
                if key not in ['updated_at', 'created_at']:
                    setattr(self, key, val)

    @staticmethod
    def parse_datetime(value):
        """Parse datetime from ISO format or return current UTC time."""
        if isinstance(value, str):
            try:
                return datetime.fromisoformat(value)
            except ValueError:
                raise ValueError(f"Invalid datetime format for: {value}")
        return value

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def __str__(self):
        """String representation of the BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())
