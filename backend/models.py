from sqlalchemy import Column, Integer, String, Text
from database import Base  

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)



class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)
    style = Column(String, nullable=False)
