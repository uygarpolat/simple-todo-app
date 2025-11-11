from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = 'sqlite:///todosapp.db' # sqlite (the todosaspp.db file that you can find in the same directory is for sqlite)
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password@localhost:5432/TodoApplicationDatabase' # postgresql
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase' # msql


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

