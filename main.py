from config import database as db
from models.estudiante import Estudiante
from schemas.estudiante import EstudianteResponse, EstudianteCreate, EstudianteUpdate
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app = FastAPI(docs_url=None, redoc_url=None)
db.init()

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
)


@app.post("/estudiantes/", response_model=EstudianteResponse)
def crear_estudiante(estudiante: EstudianteCreate, db: Session = Depends(db.get)):
    db_estudiante = Estudiante(**estudiante.model_dump())
    db.add(db_estudiante)
    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@app.get("/estudiantes/", response_model=list[EstudianteResponse])
def obtener_estudiantes(skip: int = 0, limit: int = 10, db: Session = Depends(db.get)):
    estudiantes = db.query(Estudiante).offset(skip).limit(limit).all()
    return estudiantes

@app.get("/estudiantes/{estudiante_id}", response_model=EstudianteResponse)
def obtener_estudiante(estudiante_id: int, db: Session = Depends(db.get)):
    estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    return estudiante

@app.put("/estudiantes/{estudiante_id}", response_model=EstudianteResponse)
def editar_estudiante(estudiante_id: int, estudiante: EstudianteUpdate, db: Session = Depends(db.get)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    estudiante_data = estudiante.model_dump(exclude_unset=True)
    for key, value in estudiante_data.items():
        setattr(db_estudiante, key, value)

    db.commit()
    db.refresh(db_estudiante)
    return db_estudiante

@app.delete("/estudiantes/{estudiante_id}", response_model=EstudianteResponse)
def eliminar_estudiante(estudiante_id: int, db: Session = Depends(db.get)):
    db_estudiante = db.query(Estudiante).filter(Estudiante.id_estudiante == estudiante_id).first()
    
    if db_estudiante is None:
        raise HTTPException(status_code=404, detail="Id de estudiante no encontrado")
    
    db.delete(db_estudiante)
    db.commit()
    return db_estudiante
    
    