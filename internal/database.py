from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def init_session():
    URL = "postgresql://user:password@localhost:5432/db"
    engine = create_engine(URL, connect_args={"check_same_thread": False})
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


open_session = init_session()
Base = declarative_base()
