from pydantic import BaseModel

class UsuarioBase(BaseModel):
    id_empleado: int
    nombre_usuario: str


class UsuarioCreate(UsuarioBase):
    contrasena: str


class UsuarioResponse(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True
