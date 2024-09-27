
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City

class DBStorage:
    """This class manages storage of hbnb models in MySQL."""
    
    __engine = None
    __session = None
    
    def __init__(self):
        """Create engine linked to the MySQL database."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True)
        
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects in the database session or filter by class."""
        if cls:
            objs = self.__session.query(cls).all()
        else:
            objs = self.__session.query(State).all() + self.__session.query(City).all()
        
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in objs}
    
    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)
    
    def save(self):
        """Commit changes to the current database session."""
        self.__session.commit()
    
    def delete(self, obj=None):
        """Delete the object from the current session if it's not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reloads all tables and creates a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)
