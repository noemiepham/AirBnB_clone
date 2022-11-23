#!/usr/bin/python3
"""New engine DBStorage: (models/engine/db_storage.py)"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv


class DBStorage():
    """the DBStorage class"""

    __engine = None
    __session = None

    def __init__(self):
        self._engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                     .format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB"),
                                             pool_pre_ping=True))
        if getenv('HBNB_ENV') == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session)
        all objects depending of the class name (argument cls)"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        new_dict = {}
        all_cls = [User, State, City, Amenity, Place, Review]
        list_object = []
        if cls is None:
            for i in range(len(all_cls)):
                list_object += self.__session.query(all_cls[i]).all()
        else:
            list_object += self.__session.query(cls).all()
        for element in list_object:
            key = "{}.{}".format(element.__class__.__name__, element.id)
            new_dict[key] = element
        return new_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create database and reload"""
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """remove method: remove the session"""
        self.__session.close()
