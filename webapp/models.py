from sqlalchemy import Column, Integer, Text, ForeignKey, Time, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text, ForeignKey('sessions.session_id'))
    page = Column(Text, nullable=False)
    time = Column(Time, default=dt.utcnow().time())
    date = Column(Date, default=dt.utcnow().date())


class Session(Base):
    __tablename__ = 'sessions'
    uid = Column(Integer, primary_key=True)
    session_id = Column(Text, nullable=False)
    requests = relationship("Request")


