from pydantic import BaseModel, EmailStr
from typing import Optional


class GradoBase(BaseModel):
    nombre_grado: str
    descripcion: Optional[str] = None
    cupo_maximo: int


class GradoCreate(GradoBase):
    pass
