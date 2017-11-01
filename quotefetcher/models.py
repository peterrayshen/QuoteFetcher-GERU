from sqlalchemy import Column, Integer, Text, ForeignKey, Time, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Request(Base):
    """Model of a view request"""
    __tablename__ = 'requests'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text, ForeignKey('sessions.session_id'))
    page = Column(Text, nullable=False)
    time = Column(Time, nullable=False)
    date = Column(Date, nullable=False)


class Session(Base):
    """Model of a user's browsing session"""
    __tablename__ = 'sessions'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text, nullable=False)
    requests = relationship("Request")
