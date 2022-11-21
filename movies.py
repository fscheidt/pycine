from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()

class Movie(BaseModel):
    # todos os campos sao required:
    id: int
    title: str
    year: int
    genre: str
    # se year for um campo opcional:
    # year: Union[int, None] = None

# TODO: fazer um select * from movies...
table_movies = [
    Movie(
        id=1000, 
        title="Avatar", 
        year=2009, 
        genre="drama"
    ),
    Movie(
        id=2000, 
        title="Matrix", 
        year=2019, 
        genre="sci-fi"
    )
]
# TODO: criar um endpoint e retornar a lista 
# de movies
@app.get("/movies")
async def get_movies():
    return table_movies

# post habilita o envio de dados para 
# o servidor
@app.post("/movie/")
async def create_movie(movie: Movie):
    # TODO: INSERT into movies ...
    return {'msg': 'ok movie add'}
    # return movie

# eh valido usar a mesma url desde que as
# requisicoes sejam diferentes (get e post)
@app.get("/movie/{id}")
async def get_movie_by_id():
    return {}


# uvicorn movies:app --reload