from models.estudiante import Estudiante
from schemas.estudiante import EstudianteResponse, EstudianteCreate, EstudianteUpdate
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from config import database as db



def crear(estudiante, db):
    db_estudiante = Estudiante(**estudiante.model_dump())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante


def obtener(skip, limit, db):
    estudiantes = db.query(Estudiante).offset(skip).limit(limit).all()
    return estudiantes


def obtener_id(estudiante_id, db):
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    return estudiante


def editar(estudiante_id, estudiante, db):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    estudiante_data = estudiante.model_dump(exclude_unset=True)
    for key, value in estudiante_data.items():
        setattr(db_estudiante, key, value)

    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante


def eliminar(estudiante_id, db):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    db.delete(db_estudiante)
    db.commit()
    return db_estudiante
    
    