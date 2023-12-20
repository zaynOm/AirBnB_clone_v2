#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from models import storage

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete, delete-orphan")

    @property
    def cities(self):
        cities_in_state = []
        all_cities = storage.all(City)
        for _, v in all_cities.items():
            if v.state_id == self.id:
              cities_in_state.append(v)
        return cities_in_state
