from pydantic import BaseModel
from typing import Optional

class GeneroModel(BaseModel):
    id_genero: Optional[int]
    nombre_genero: str
    descripcion: str