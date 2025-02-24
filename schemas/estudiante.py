from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from enum import Enum


class EstratoEnum(str, Enum):
    uno = "1"
    dos = "2"
    tres = "3"
    cuatro = "4"
    cinco = "5"


class EstudianteBase(BaseModel):
    nombre: str
    apellido: str
    documento_identidad: str
    fecha_nacimiento: date
    email: EmailStr
    telefono: Optional[str] = None
    estrato: EstratoEnum
    direccion: Optional[str] = None


class EstudianteCreate(EstudianteBase):
    pass



class EstudianteResponse(EstudianteBase):
    id_estudiante: int

    class Config:
        from_attributes = True