from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'

    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    id_empleado = Column(Integer, ForeignKey('administrativos.id_administrativo', ondelete='CASCADE'), nullable=False)
    nombre_usuario = Column(String(50), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)

    administrativo = relationship("Administrativo", back_populates="usuarios")