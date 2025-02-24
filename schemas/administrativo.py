from pydantic import BaseModel, EmailStr
from typing import Optional


class AdministrativoBase(BaseModel):
    nombre: str
    apellido: str
    documento_identidad: str
    cargo: str
    email: EmailStr
    telefono: Optional[str] = None


class AdministrativoCreate(AdministrativoBase):
    pass

