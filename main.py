from config import database as db
from models.estudiante import Estudiante
from schemas.estudiante import EstudianteResponse, EstudianteCreate, EstudianteUpdate
from models.administrativo import Administrativo
from models.usuario import Usuario
from sqlalchemy.orm import Session
from models.grado import Grado
from models.solicitud_matricula import SolicitudMatricula
from routers import estudiante_router, auth_router, solicitud_matricula_router
from fastapi import FastAPI, Depends, HTTPException
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)

app = FastAPI(docs_url=None, redoc_url=None)

# Inicializar la base de datos
db.init()  # Esto debería configurar la conexión a la base de datos
db.Base.metadata.create_all(bind=db.engine)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://unpkg.com/swagger-ui-dist@5/swagger-ui.css",
)


app.include_router(estudiante_router.router)
app.include_router(auth_router.router)
app.include_router(solicitud_matricula_router.router)
    