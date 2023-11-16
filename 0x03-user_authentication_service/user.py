#!/usr/bin/env python3
''' a simple user model'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    '''the user model'''
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(250), nullable=False)
    hashed_password = Column('hashed_password', String(250), nullable=False)
    session_id = Column('session_id', String(250), nullable=True)
    reset_token = Column('reset_token', String(250), nullable=True)
