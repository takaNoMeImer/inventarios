from database.config import conn

def mostrar_libros():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    results = cursor.fetchall()
    cursor.close()
    return {
        "data": results
    }