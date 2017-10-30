from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text, ForeignKey('session.session_id'))
    page = Column(Text, nullable=False)
    date = Column(Text)
    time = Column(Text)


class Session(Base):
    __tablename__ = 'session'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text)
    requests = relationship("Request")


