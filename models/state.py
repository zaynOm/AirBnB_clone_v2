#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    # this runs if the engine is FileStorage
    else:
        name = ''

        @property
        def cities(self):
            """ Return the list of City instances with state_id equals the current State.id
                FileStorage between State and City """
            from models import storage
            cities = []
            cls_list = storage.all(City)
            for v in cls_list.values():
                if v.state_id == self.id:
                    cities.append(v)
            return cities
