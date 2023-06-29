from database.config import conn
from models.autor_model import AutorModel

def mostrar_autores():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM autores")
    results = cursor.fetchall()
    cursor.close()
    return {
        "data": results
    }

def insertar_autor(autor: AutorModel):
    cursor = conn.cursor()
    try:
        query = "INSERT INTO autores (codigo_autor, nombre_autor, nacionalidad_autor) VALUES (%s,%s,%s)"
        cursor.execute(query, (autor.codigo_autor, autor.nombre_autor, autor.nacionalidad_autor))
        conn.commit()
        return {"message": "Autor creado con exito"}
    finally:
        if cursor:
            cursor.close()