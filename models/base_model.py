#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):

        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, tform))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
