from fastapi import APIRouter
from controllers.controller_autores import mostrar_autores, insertar_autor
from models.autor_model import AutorModel

routes_autores = APIRouter(prefix="/autores")

@routes_autores.get("/all")
async def all():
    return mostrar_autores()

@routes_autores.post("/crear")
async def crear(autor: AutorModel):
    return insertar_autor(autor)