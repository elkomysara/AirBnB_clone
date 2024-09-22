#!/usr/bin/python3
"""Defines the FileStorage class for JSON serialization and deserialization."""

import json
from models.base_model import BaseModel
from models.user import User  # Import the User class

class FileStorage:
    """Handles storage of objects in JSON format."""
    
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if the JSON file exists)."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        self.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
