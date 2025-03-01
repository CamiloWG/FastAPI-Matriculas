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

# IMPORTAR LOS MODELOS EN ORDEN CORRECTO
from models.administrativo import Administrativo
from models.usuario import Usuario

def init():
    """Inicializa la base de datos y crea las tablas si no existen."""
    Base.metadata.create_all(bind=engine)

def get():
    """Obtiene una sesión de la base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
