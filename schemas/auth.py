from pydantic import BaseModel, EmailStr

class LoginRequest(BaseModel):
    nombre_usuario: str
    contrasena: str

class LoginResponse(BaseModel):
    id_usuario: int
    mensaje: str

class PasswordResetRequest(BaseModel):
    email: EmailStr
