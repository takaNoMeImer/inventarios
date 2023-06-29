from pydantic import BaseModel

class EditorialModel(BaseModel):
    codigo_editorial: str
    nombre_editorial: str
    contacto: str
    telefono: str