from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text)
    page = Column(Text, nullable=False)
    date = Column(Text)
    time = Column(Text)

