from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# SQLALCHEMY_DATABASE_URL = 'sqlite:///todosapp.db' # test sqlite (the todosaspp.db file that you can find in the same directory is for sqlite)
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/TodoApplicationDatabase' # test postgresql
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase' # test mysql

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

