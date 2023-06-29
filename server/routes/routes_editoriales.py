from fastapi import APIRouter
from controllers.controller_editoriales import mostrar_editoriales, insertar_editorial
from models.editorial_model import EditorialModel

routes_editoriales = APIRouter(prefix="/editoriales")

@routes_editoriales.get("/all")
async def all():
    return mostrar_editoriales()

@routes_editoriales.post("/crear")
async def crear(editorial: EditorialModel):
    return insertar_editorial(editorial)
