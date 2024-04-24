#!/usr/bin/python3
'''City class'''


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
import sqlalchemy


class City(Base):
    '''City representation'''
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
