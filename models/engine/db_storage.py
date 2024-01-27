#!/usr/bin/python3
"Database storage engine"
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DbStorage:
    """"""

    __engine = None
    __session = None

    def __init__(self):
        "Initiate the DB connection"
        db_user = getenv("HBNB_MYSQL_USER")
        db_pwd = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        env_mode = getenv("HBNB_ENV")
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                db_user, db_pwd, db_host, db_name
            ),
            pool_pre_ping=True,
        )
        if env_mode == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        "Fetchs all tables or only the ones with the same class name as cls"
        classes = [State, City, User, Place, Review]
        result = {}
        objs = []
        if cls:
            objs = self.__session.query(cls).all()
        else:
            for c in classes:
                objs += self.__session.query(c).all()

        for obj in objs:
            key = obj.__class__.__name__ + "." + obj.id
            result[key] = obj

        return result

    def new(self, obj):
        "Add an object to the database session"
        self.__session.add(obj)

    def save(self):
        "Commit all changes to the database session"
        self.__session.commit()

    def delete(self, obj=None):
        "Delete object if not None from the database session"
        if obj:
            self.__session.delete(obj)

    def reload(self):
        "Create all tables in database and create a session"
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        "Close database connection"
        self.__session.close()
