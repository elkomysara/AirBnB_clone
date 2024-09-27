
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
import os

class DBStorage:
    """DBStorage engine for handling MySQL database storage"""
    
    __engine = None
    __session = None

    def __init__(self):
        """Create engine with environment variables"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current database session all objects of a specific class"""
        query_dict = {}
        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = obj.__class__.__name__ + '.' + obj.id
                query_dict[key] = obj
        else:
            for _class in [State, City]:
                objects = self.__session.query(_class).all()
                for obj in objects:
                    key = obj.__class__.__name__ + '.' + obj.id
                    query_dict[key] = obj
        return query_dict

    def new(self, obj):
        """Add the object to the current session"""
        self.__session.add(obj)

    def save(self):
        """Commit the changes of the current session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database and create all tables"""
        from models.state import State
        from models.city import City
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
