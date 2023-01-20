from database import Base
from sqlalchemy import String, Boolean,Integer,Column,Text

class baby(Base):
    __tablename__ = 'babyTable'
    id=Column(Integer,primary_key=True)
    gender = Column(String)
    babyName = Column(String)
    category = Column(String)
    meaning = Column(String)


    def __repr__(self):
        return f"<Item name={self.babyName} category={self.category}>"