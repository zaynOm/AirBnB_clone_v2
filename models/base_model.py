#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from hashlib import md5
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from models import storage_type

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            fmt = '%Y-%m-%dT%H:%M:%S.%f'
            for k, v in kwargs.items():
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(v, fmt))
                elif k != '__class__':
                    setattr(self, k, v)

    def __str__(self):
        """Returns a string representation of the instance"""
        obj_info = self.__dict__.copy()
        obj_info.pop('_sa_instance_state')
        cls = self.__class__.__name__
        if storage_type == 'db' and (pwd := self.__dict__.get('password')):
            self.__dict__['password'] = md5(pwd.encode()).hexdigest()
        return f"[{cls}] ({self.id}) {obj_info}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        if dictionary.get("_sa_instance_state"):
            del dictionary["_sa_instance_state"]

        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
