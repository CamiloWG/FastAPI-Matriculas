from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.auth import LoginRequest, LoginResponse, PasswordResetRequest
from services.auth_service import autenticar_usuario, recuperar_contrasena
from config import database as db

router = APIRouter(prefix="/auth", tags=["Autenticación"])

@router.post("/login", response_model=LoginResponse)
def login(request: LoginRequest, db: Session = Depends(db.get)):
    return autenticar_usuario(request, db)

@router.post("/password-reset")
def reset_password(request: PasswordResetRequest, db: Session = Depends(db.get)):
    return recuperar_contrasena(request, db)
