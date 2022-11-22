from fastapi import FastAPI
from fastapi.middleware.cors import (
     CORSMiddleware
)
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

# /artista/arnold sch

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
