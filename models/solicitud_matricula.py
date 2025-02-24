from config.database import Base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Text
from sqlalchemy.orm import relationship

class SolicitudMatricula(Base):
    __tablename__ = 'solicitud_matricula'

    id_solicitud = Column(Integer, primary_key=True, autoincrement=True)
    id_estudiante = Column(Integer, ForeignKey('estudiantes.id_estudiante', ondelete='CASCADE'), nullable=False)
    id_administrativo = Column(Integer, ForeignKey('administrativos.id_administrativo', ondelete='SET NULL'), nullable=True)
    id_grado = Column(Integer, ForeignKey('grados.id_curso', ondelete='CASCADE'), nullable=False)
    fecha_solicitud = Column(Date, nullable=False)
    estado = Column(Enum('Pendiente', 'Aprobada', 'Rechazada'), nullable=False, default='Pendiente')

    estudiante = relationship("Estudiante", back_populates="solicitudes")
    administrativo = relationship("Administrativo", back_populates="solicitudes")
    grado = relationship("Grado", back_populates="solicitudes")