from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union

app = FastAPI()
# Fazer o mapeamento ORM
# Mapeamento Movie
# Atributos:
# - id
# - title
# - year 
# - genre

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
    )
]
# TODO: criar um endpoint e retornar a lista 
# de movies
@app.get("/movies")
async def get_movies():
    return table_movies

# uvicorn movies:app --reload


# Exercício:
# funcionarios.py
# mapear a entidade funcionario
# - nome, admissao, salario
# - /funcionarios (listar)
# - /funcionarios (salario > 6000)


