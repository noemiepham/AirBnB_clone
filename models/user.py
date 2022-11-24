#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    #Task8:places must represent a relationship with the class Place. If the User object is deleted,
    places = relationship("Place", backref="user", cascade="all, delete")

    #Task 9: class attribute reviews must represent a relationship with the class Review
    reviews = relationship("Review", backref="user", cascade="all, delete")
    
