
from datetime import datetime
import models
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class BaseModel:
    """The BaseModel class defines all common attributes/methods for other classes"""
    
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    def __init__(self, *args, **kwargs):
        """Initialize a new model instance."""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
    
    def save(self):
        """Updates `updated_at` and saves the instance to storage."""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        my_dict = self.__dict__.copy()
        if '_sa_instance_state' in my_dict:
            del my_dict['_sa_instance_state']
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def delete(self):
        """Deletes the current instance from storage."""
        models.storage.delete(self)
