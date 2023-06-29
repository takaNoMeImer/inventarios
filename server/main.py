from fastapi import FastAPI
from routes.routes_autores import routes_autores
from routes.routes_editoriales import routes_editoriales
from routes.routes_generos import routes_generos
from routes.routes_libros import routes_libros
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Welcome API"
    }

app.include_router(routes_autores)
app.include_router(routes_generos)
app.include_router(routes_libros)
app.include_router(routes_editoriales)