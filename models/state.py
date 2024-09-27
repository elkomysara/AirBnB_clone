
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """The state class, contains name and cities relationship."""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        """Getter for FileStorage relationship between State and City."""
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
