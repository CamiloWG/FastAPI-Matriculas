import os

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_name = "../db.sqlite"
db_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{os.path.join(db_dir, db_name)}"

engine = create_engine(db_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, bind=engine, autoflush=False)

Base = declarative_base()

Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()