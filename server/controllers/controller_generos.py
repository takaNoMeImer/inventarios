from database.config import conn
from models.genero_model import GeneroModel

def mostrar_generos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM generos")
    results = cursor.fetchall()
    cursor.close()
    return {
        "data": results
    }

def insertar_genero(genero: GeneroModel):
    cursor = conn.cursor()
    try:
        query = "INSERT INTO generos (nombre_genero, descripcion) VALUES (%s,%s)"
        cursor.execute(query, (genero.nombre_genero, genero.descripcion))
        conn.commit()
        return {"message": "Genero creado con exito"}
    finally:
        if cursor:
            cursor.close()