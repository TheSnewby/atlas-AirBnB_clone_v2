#!/usr/bin/python3
"""This module initializes the package and instantiates the FileStorage object."""

from models.engine.file_storage import FileStorage
# from models.base_model import BaseModel, Base
# from models.user import User
# from models.place import Place
# from models.city import City  # Import the City class

# Instantiate the FileStorage object
storage = FileStorage()
storage.reload()

# Optionally, expose models for easy access
__all__ = ['BaseModel', 'User', 'Place', 'City', 'storage']
