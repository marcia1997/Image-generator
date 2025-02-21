from sqlalchemy import Column, Integer, String, Text
from database import Base

class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    prompt = Column(Text, nullable=False)  # User's input text
    image_url = Column(String, nullable=False)  # URL of generated image
    style = Column(String, nullable=False)  # Chosen artistic style
