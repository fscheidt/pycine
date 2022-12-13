from fastapi import FastAPI
from fastapi.middleware.cors import (
     CORSMiddleware
)
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

# Precisamos importar MovieUtils e Genre:
from tmdb.models import Genre
from tmdb.api_utils import (
    RequestApi, MovieUtils
)
app = FastAPI()
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

from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

# todo: testar para ver se o banco nao esta sendo 
# apagado toda vez que inicia o fastapi
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from pydantic import BaseModel

# instalar sqlAlchemy para ORM
# pip install sqlalchemy
class User(BaseModel):
    name: str
    email: str
    password: str

@app.post("/user/create")
def create_user(user: User, db: Session = Depends(get_db)):
    # verifica se ja nao um usuario com este email

    # db = get_db()
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Email already registered"
        )
    # faz o insert no banco
    status = crud.create_user(db=db, user=user)
    print(status)
    return status



    print(user)
    return "Usuario criado com sucesso"

# fornecido um id, retorno o 
# json do filme
# /movie/1
@app.get("/movie/{id}")
async def get_movie(id: int):
    import json
    # lista de dictionary
    data = json.load(open('filmes.json'))
    for filme in data:
        if filme['id'] == id:
            return filme
    return {}

# TODO: get_genres

@app.get("/movies_json")
async def get_movies_json():
    import json
    data = json.load(open('filmes.json'))
    return data

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
    return {"msg": "Hello"}

# rodar o fastapi:
# uvicorn main:app --reload

# pip install -r requirements.txt
# source env/
# pip install fastapi uvicorn
