from sqlalchemy import Column, Integer, String, DateTime,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


Base = declarative_base()
metadata = Base.metadata

class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('author.id'))
    year = Column(Integer)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    
    author = relationship('Author')
    
class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now()) 