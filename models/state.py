#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete, delete-orphan")

    @cities
    def cities(self):
        cities = []
        cls_list = storage.all(City)
        for k, v in cls_list.items():
            if v.state_id == self.id:
              cities.append(v)
        return cities
