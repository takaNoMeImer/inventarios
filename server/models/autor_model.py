from pydantic import BaseModel

class AutorModel(BaseModel):
    codigo_autor: str
    nombre_autor: str
    nacionalidad_autor: str