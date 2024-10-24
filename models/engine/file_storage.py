#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import os

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models (of a class) currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        # If cls is provided, filter by class
        if cls and cls in classes.values():
            cls_dict = {key: value for key, value in
                         FileStorage.__objects.items()
                         if isinstance(value, cls)}
            return cls_dict
        else:
            return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary."""
        FileStorage.__objects[obj.to_dict()['__class__'] + '.' + obj.id] = obj

    def save(self):
        """Saves storage dictionary to file."""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {key: val.to_dict() for key, val in FileStorage.__objects.items()}
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel, 'User': User, 'Place': Place,
            'State': State, 'City': City, 'Amenity': Amenity,
            'Review': Review
        }

        # Ensure the file exists
        if not os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'w') as f:
                json.dump({}, f)  # Create an empty file if it doesn't exist

        try:
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    FileStorage.__objects[key] = classes[val['__class__']](**val)
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle the case where the file might be empty or unreadable
            pass

    def delete(self, obj=None):
        """Deletes an object from storage."""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
            else:
                print("** no instance found **")
