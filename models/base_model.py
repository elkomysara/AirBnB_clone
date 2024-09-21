#!/usr/bin/python3
"""Base model module"""
from datetime import datetime

class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Initialize the BaseModel with datetime and unique id"""
        self.id = "1234"
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """Update the updated_at attribute to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of instance"""
        return {
            "id": self.id,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "__class__": "BaseModel"
        }
