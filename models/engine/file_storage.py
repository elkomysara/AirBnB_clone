#!/usr/bin/python3
"""Module that defines the FileStorage class."""
import json
from models.base_model import BaseModel

class FileStorage:
    """Class for serializing instances to a JSON file and deserializing from JSON file."""
    
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
        """Deserializes the JSON file to __objects, only if the JSON file exists."""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
                for key, obj in obj_dict.items():
                    # Assuming only BaseModel for now, you can add more types later.
                    self.__objects[key] = BaseModel(**obj)
        except FileNotFoundError:
            pass
