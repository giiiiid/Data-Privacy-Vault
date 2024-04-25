from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URI = "sqlite:///./dpa.db"


'''an engine to connect our database'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread":False}
)


'''session local to handle our committed messages'''
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)


'''declaring our database'''
Base = declarative_base()