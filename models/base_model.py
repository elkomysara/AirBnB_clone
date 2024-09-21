#!/usr/bin/python3
"""Base model module"""

class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Initialize the BaseModel"""
        self.id = "1234"
        self.created_at = "2023-09-21"
        self.updated_at = "2023-09-21"

    def save(self):
        """Simulate saving the model"""
        self.updated_at = "2023-09-21"

    def to_dict(self):
        """Returns dictionary representation of instance"""
        return {
            "id": self.id,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "__class__": "BaseModel"
        }
