from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from enum import Enum

class EstadoSolicitudEnum(str, Enum):
    pendiente = "Pendiente"
    aprobada = "Aprobada"
    rechazada = "Rechazada"


class SolicitudMatriculaBase(BaseModel):
    id_estudiante: int
    id_administrativo: Optional[int] = None
    id_grado: int
    fecha_solicitud: date
    estado: EstadoSolicitudEnum = EstadoSolicitudEnum.pendiente


class SolicitudMatriculaCreate(SolicitudMatriculaBase):
    pass

