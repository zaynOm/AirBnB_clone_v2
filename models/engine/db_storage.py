#!/usr/bin/python3
""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review



class DbStorage:
    ""
    __engine = None
    __session = None

    def __init__(self):
        "Initiate the DB connection"
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        #HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV ')
        self.__engine = create_engine('mysql+mysqldb://{}:{}/localhost/{}'
                                      .format(
                                          HBNB_MYSQL_USER,
                                          HBNB_MYSQL_PWD,
                                          HBNB_MYSQL_DB
                                      ), pool_pre_ping=True)
        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        ""
        print('this is running')
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(User, State, City, Amenity, Place, Review).all()

        result = {}
        for obj in objs:
            # TODO: make a dict of class.id: obj
            print('Objects from db: ', obj)
        
        return {'test dict': 'OK'}

    def add(self, obj):
        ""
        self.__session.add(obj)

    def save(self):
        ""
        self.__session.commit()

    def delete(self, obj=None):
        ""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        ""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
