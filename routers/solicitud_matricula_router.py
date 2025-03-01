from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from config.database import get
from services.solicitud_matricula_service import listar_solicitudes, obtener_solicitud, crear_solicitud, eliminar_solicitud
from schemas.solicitud_matricula import SolicitudMatriculaCreate, SolicitudMatriculaResponse

router = APIRouter(prefix="/solicitudes", tags=["Solicitudes de Matrícula"])

@router.get("/", response_model=list[SolicitudMatriculaResponse])
def get_solicitudes(db: Session = Depends(get)):
    return listar_solicitudes(db)

@router.get("/{id_solicitud}", response_model=SolicitudMatriculaResponse)
def get_solicitud(id_solicitud: int, db: Session = Depends(get)):
    return obtener_solicitud(id_solicitud, db)

@router.post("/", response_model=SolicitudMatriculaResponse)
def post_solicitud(solicitud: SolicitudMatriculaCreate, db: Session = Depends(get)):
    return crear_solicitud(solicitud, db)

@router.delete("/{id_solicitud}")
def delete_solicitud(id_solicitud: int, db: Session = Depends(get)):
    return eliminar_solicitud(id_solicitud, db)
