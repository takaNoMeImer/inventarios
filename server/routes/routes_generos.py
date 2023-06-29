from fastapi import APIRouter
from controllers.controller_generos import mostrar_generos, insertar_genero
from models.genero_model import GeneroModel

routes_generos = APIRouter(prefix="/generos")

@routes_generos.get("/all")
async def all():
    return mostrar_generos()

@routes_generos.post("/crear")
async def crear(genero: GeneroModel):
    return insertar_genero(genero)