from fastapi import FastAPI
from fastapi.middleware.cors import (
     CORSMiddleware
)
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from sqlalchemy.orm import Session

# Importa classes para persistencia dos dados no SQLite
import crud, models
from schemas import UserModel
from database import SessionLocal, engine

# Importar MovieUtils e Genre para usar na api do TMDB
from tmdb.models import Genre
from tmdb.api_utils import (
    RequestApi, MovieUtils
)
app = FastAPI()

# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# todo: testar para ver se o banco nao esta sendo 
# apagado toda vez que inicia o fastapi
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# =============================
# USER (sqlite)
# =============================

@app.post("/user/create")
def create_user(user: UserModel, db: Session = Depends(get_db)):
    # verifica se ja nao um usuario com este email
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
    # faz o insert no banco
    new_user = crud.create_user(db=db, user=user)
    # print(new_user)
    return new_user


# =============================
# MOVIE (tmdb)
# =============================

@app.get("/movies")
async def get_movies():
    # chamar a classe MovieUtils para consultar TMDB
    movies = MovieUtils.get_movies(Genre.Scifi.value)
    return movies

@app.get("/artista/id/{id}")
async def get_artista(id):
    artista = RequestApi.get_artista(id)
    return artista

# Objetivo: Implementar o endpoint para 
# encontrar artistas pelo nome fornecido como 
# parametro na url.
# - Retorna uma lista de artistas.
# - Exemplo de endpoint na nossa API:
# /artista/name/arnold

@app.get("/find/{title}/{genre}")
async def find(title: str, genre):
    import json
    data = json.load(open('filmes.json'))
    encontrou = []
    for filme in data:
        # in - contains (ou contem um substring)
        if title.lower() in filme['title'].lower():
            # append - adiciona na lista
            encontrou.append(filme)
    return encontrou

@app.get("/")  # HTTP GET
async def home():
    return {"msg": "pycine back-end"}

# rodar o fastapi:
# uvicorn main:app --reload

# pip install -r requirements.txt
# source env/
# pip install fastapi uvicorn
