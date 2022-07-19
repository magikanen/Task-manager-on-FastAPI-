import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

"""
from sqlalchemy.engine.url import URL
DATABASE = {
    'drivername': 'postgresql',
    'host': 'db',
    'port': '5432',
    'username': 'mgknn',
    'password': 'tst',
    'database': 'postgres'
}
engine = create_engine(URL(**DATABASE))
"""
engine = create_engine(os.getenv('DATABASE_URL'))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_session():
   try:
       db = SessionLocal()
       yield db
   finally:
       db.close()
