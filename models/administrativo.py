from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship


class Administrativo(Base):
    __tablename__ = 'administrativos'

    id_administrativo = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    documento_identidad = Column(String(11), unique=True, nullable=False)
    cargo = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    telefono = Column(String(20))

    solicitudes = relationship("SolicitudMatricula", back_populates="administrativo")
    usuarios = relationship("Usuario", back_populates="administrativo")