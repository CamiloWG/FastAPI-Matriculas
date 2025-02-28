from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

estrato_enum = Enum('1', '2', '3', '4', '5', name='estrato_enum')

class Estudiante(Base):
    __tablename__ = 'estudiantes'

    id_estudiante = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    documento_identidad = Column(String(11), unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    email = Column(String(100), nullable=False)
    telefono = Column(String(10))
    estrato = Column(estrato_enum, nullable=False)
    direccion = Column(Text)

    #solicitudes = relationship("SolicitudMatricula", back_populates="estudiante")