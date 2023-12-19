#!/usr/bin/python3
""" DBStorage Engine that handels the DataBase Storage Engine """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.base_model import Base
from models.place import Place


if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.place import place_amenity

classes = {"User": User, "Amenity": Amenity, "Review": Review, \
       "Place": Place, "City": City, "State": State}

class DBStorage:
    """ Class that handels Data Base Storage for mysql """
    __engine = None
    __session = None

    def __init__(self):
        """ instantiate new database storage instance """
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, \
                                                 HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ retreives a query on the DB session """
        dct ={}
        if cls is None:
            for c in classes.values():
                objs = self.__session.query(c).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    dct[key] = obj
        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = obj.__class__.__name__ = '.' + obj.id
                dct[key] = obj
        return dct

    def new(self, obj):
        """ adds the obj to the current DB session """
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """ sves all the changes to the DB session using commit() """
        self.__session.commit()

    def delete(self, obj=None):
        """ delets form the current DB session the obj if not null """
        if obj is not None:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id).delete()

    def reload(self):
        """ reloads the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """ Close the current SQLAlchemy session """
        self.__session.close()
