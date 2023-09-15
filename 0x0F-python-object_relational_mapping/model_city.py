#!/usr/bin/python3
""" base city """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ city class """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = column(Integer, nullable=False, ForeignKey("states.id"))
