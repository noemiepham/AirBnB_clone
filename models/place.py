#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models import storage
from models.review import Review
from models.amenity import Amenity

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             nullable=False, primary_key=True),
                      Column("amenity_id", String(60),
                             ForeignKey("amenity.id"),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    # task 9: class attribute reviews must represent a relationship with the class Review

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place",
                               cascade="all,delete")
    else:
        @ property
        def reviews(self):
            """getter method for reviews"""
            reviews_list = []
            all_review = storage.all(Review)
            for element in all_review.values():
                if element.place_id == self.id:
                    reviews_list.append(element)
                return reviews_list

    # tast 10:
    # Add an instance of SQLAlchemy Table called place_amenity for
    # creating the relationship Many-To-Many between Place and Amenity:
    if getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", backref="place_amenity",
                                 secondary=place_amenity, viewonly=False)
    else:
        @property
        def amenities(self):
            """getter method for reviews"""
            amenities_list = []
            all_amenities = storage.all(Review)
            for element in all_amenities.values():
                if element.place_id == self.id:
                    amenities_list.append(element)
            return amenities_list

        @amenities.setter
        def amenities(self, cls):
            if not isinstance(cls, Amenity):
                return
            self.amenity_ids.append(cls.id)
