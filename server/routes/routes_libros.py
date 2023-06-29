from fastapi import APIRouter
from controllers.controller_libros import mostrar_libros
from models.libro_model import LibroModel

routes_libros = APIRouter(prefix="/libros")

@routes_libros.get("/all")
async def all():
    return mostrar_libros()