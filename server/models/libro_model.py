from pydantic import BaseModel

class LibroModel(BaseModel):
    codigo_libro: str
    nombre_libro: str
    existencias: int
    precio: float
    codigo_autor: str
    codigo_editorial: str
    id_genero: int
    descripcion: str