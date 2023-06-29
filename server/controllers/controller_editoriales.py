from database.config import conn
from models.editorial_model import EditorialModel

def mostrar_editoriales():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM editoriales")
    results = cursor.fetchall()
    cursor.close()
    return {
        "data": results
    }

def insertar_editorial(editorial: EditorialModel):
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT COUNT(*) FROM editoriales WHERE codigo_editorial = %s", (editorial.codigo_editorial,))
        count = cursor.fetchone()[0]
        
        if count > 0:
            return {"message": "La editorial ya existe"}

        query = "INSERT INTO editoriales (codigo_editorial, nombre_editorial, contacto, telefono) VALUES (%s,%s,%s,%s)"
        cursor.execute(query, (editorial.codigo_editorial, editorial.nombre_editorial, editorial.contacto, editorial.telefono))
        conn.commit()
        return {"message": "Editorial creada con exito"}
    finally:
        if cursor:
            cursor.close()