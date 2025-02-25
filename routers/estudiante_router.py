from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.estudiante import Estudiante
from schemas.estudiante import EstudianteResponse, EstudianteCreate, EstudianteUpdate
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from config import database as db
from services.estudiante_service import obtener, obtener_id, crear, editar, eliminar

router = APIRouter(prefix="/estudiantes", tags=["Estudiantes"])

@router.post("/", response_model=EstudianteResponse)
def crear_estudiante(estudiante: EstudianteCreate, db: Session = Depends(db.get)):
    return crear(estudiante, db)

@router.get("/", response_model=list[EstudianteResponse])
def obtener_estudiantes(skip: int = 0, limit: int = 10, db: Session = Depends(db.get)):
    return obtener(skip, limit, db)

@router.get("/{estudiante_id}", response_model=EstudianteResponse)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(db.get)):
    return obtener_id(estudiante_id, db)

@router.put("/{estudiante_id}", response_model=EstudianteResponse)
def editar_estudiante(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(db.get)):
    return editar(estudiante_id, estudiante, db)

@router.delete("/{estudiante_id}", response_model=EstudianteResponse)
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(db.get)):
    return eliminar(estudiante_id, db)
    