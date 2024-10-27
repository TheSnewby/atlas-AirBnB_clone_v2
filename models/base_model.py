#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone."""

from datetime import datetime, timezone
import uuid
import sqlalchemy
from sqlalchemy import Column, String, DateTime

class BaseModel:
    """Base class for all models in the AirBnB clone."""

    id = Column(String(60), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))

    def __init__(self, *args, **kwargs):
        """Instantiate a new model."""
        if not kwargs:
            # Set the default values if no kwargs provided
            self.created_at = datetime.now(timezone.utc)
            self.updated_at = datetime.now(timezone.utc)
        else:
            if 'id' not in kwargs:
                raise KeyError('id is required')
            
            # Assign values from kwargs or set default values
            self.id = kwargs['id']

            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            else:
                self.created_at = datetime.now(timezone.utc)

            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            else:
                self.updated_at = datetime.now(timezone.utc)

            # Clean up unwanted keys
            kwargs.pop('__class__', None)

            # Set attributes from kwargs
            for key, val in kwargs.items():
                if key not in ['updated_at', 'created_at']:
                    setattr(self, key, val)

            # Update instance dictionary with kwargs
            self.__dict__.update(kwargs)

    def to_dict(self):
        """Convert instance into dict format."""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({
            '__class__': (str(type(self)).split('.')[-1]).split('\'')[0]
        })

        # Format created_at and updated_at correctly
        dictionary['created_at'] = self.created_at.isoformat() if isinstance(self.created_at, datetime) else self.created_at
        dictionary['updated_at'] = self.updated_at.isoformat() if isinstance(self.updated_at, datetime) else self.updated_at

        # Remove SQLAlchemy-specific attributes
        dictionary.pop('_sa_instance_state', None)

        return dictionary

    def __str__(self):
        """String representation of the BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.to_dict())
