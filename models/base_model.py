
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()

class BaseModel:
    """A base class for all models using SQLAlchemy"""
    
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model, manages kwargs for SQLAlchemy"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if kwargs.get("id") is None:
                self.id = str(uuid.uuid4())
            if kwargs.get("created_at") is None:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at") is None:
                self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.utcnow()

    def save(self):
        """Saves the instance to the database"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Converts instance to a dictionary format"""
        dict_obj = self.__dict__.copy()
        if "_sa_instance_state" in dict_obj:
            del dict_obj["_sa_instance_state"]
        dict_obj['__class__'] = self.__class__.__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj

    def delete(self):
        """Delete the current instance from storage"""
        models.storage.delete(self)
