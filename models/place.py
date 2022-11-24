#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from os import environ
from models import storage
from models.city import City


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(String(1024), nullable=False)
    number_bathrooms = Column(Integer, nullable=False, defaut=0)
    max_guest = Column(Integer, nullable=False, defaut=0)
    price_by_night = Column(Integer, nullable=False, defaut=0)
    latitude = Column(float, nullable=False)
    longitude = Column(float, nullable=False)
    amenity_ids = []

    #task 9: class attribute reviews must represent a relationship with the class Review

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all,delete")
        
        #tast 10: 
        # Add an instance of SQLAlchemy Table called place_amenity for 
        # creating the relationship Many-To-Many between Place and Amenity:
        amenities = relationship("Amenity", backref="place_amenity",
                                secondary="place_amenity", viewonly=False)
    else:
        @ property
        def cities(self):
            """getter method for cities"""
            cities_dict = []
            for key in storage.all(City):
                if self.id in storage.all(City)[key].state_id:
                    cities_dict.append(storage.all(City)[key])
                return cities_dict
    
    #tast 10: 
    # Add an instance of SQLAlchemy Table called place_amenity for 
    # creating the relationship Many-To-Many between Place and Amenity:

