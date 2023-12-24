#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.city import City
from models import storage_type


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="delete, delete-orphan"
        )
    else:
        name = ""

        @property
        def cities(self):
            "Getter of the cities list that are related to the current State"
            from models import storage

            cities_in_state = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_in_state.append(city)
            return cities_in_state
