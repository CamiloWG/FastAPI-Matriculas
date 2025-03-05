from models.usuario import Usuario
from schemas.auth import LoginRequest, LoginResponse, PasswordResetRequest
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_contrasena(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def autenticar_usuario(request: LoginRequest, db: Session):
    usuario = db.query(Usuario).filter(Usuario.nombre_usuario == request.nombre_usuario).first()
    
    if not usuario or not verificar_contrasena(request.contrasena, usuario.contrasena):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

    return LoginResponse(id_usuario=usuario.id_usuario, mensaje="Inicio de sesión exitoso")

def recuperar_contrasena(request: PasswordResetRequest, db: Session):
    usuario = db.query(Usuario).filter(Usuario.email == request.email).first()
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Correo no encontrado")

    # Aquí se enviaría un correo con un enlace para restablecer la contraseña (simulado)
    return {"mensaje": "Se ha enviado un enlace de recuperación a su correo"}
