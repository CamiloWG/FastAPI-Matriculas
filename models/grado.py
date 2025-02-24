from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship



class Grado(Base):
    __tablename__ = 'grados'

    id_curso = Column(Integer, primary_key=True, autoincrement=True)
    nombre_grado = Column(String(100), nullable=False)
    descripcion = Column(Text)
    cupo_maximo = Column(Integer, nullable=False)

    solicitudes = relationship("SolicitudMatricula", back_populates="grado")