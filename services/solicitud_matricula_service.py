from sqlalchemy.orm import Session
from models.solicitud_matricula import SolicitudMatricula
from schemas.solicitud_matricula import SolicitudMatriculaCreate, SolicitudMatriculaResponse
from fastapi import HTTPException

def listar_solicitudes(db: Session) -> list[SolicitudMatriculaResponse]:
    return db.query(SolicitudMatricula).all()

def obtener_solicitud(id_solicitud: int, db: Session) -> SolicitudMatriculaResponse:
    solicitud = db.query(SolicitudMatricula).filter(SolicitudMatricula.id_solicitud == id_solicitud).first()
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    return solicitud

def crear_solicitud(solicitud: SolicitudMatriculaCreate, db: Session) -> SolicitudMatriculaResponse:
    nueva_solicitud = SolicitudMatricula(**solicitud.dict())
    db.add(nueva_solicitud)
    db.commit()
    db.refresh(nueva_solicitud)
    return nueva_solicitud

def eliminar_solicitud(id_solicitud: int, db: Session):
    solicitud = db.query(SolicitudMatricula).filter(SolicitudMatricula.id_solicitud == id_solicitud).first()
    if not solicitud:
        raise HTTPException(status_code=404, detail="Solicitud no encontrada")
    
    db.delete(solicitud)
    db.commit()
    return {"message": "Solicitud eliminada correctamente"}
