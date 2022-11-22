"""
no caso de ocorrer o erro "ModuleNotFound", abrir o terminal (na pasta do projeto) e rodar o comando:

export PYTHONPATH=.

"""
from tmdb.models import Genre
from tmdb.api_utils import (
    RequestApi, MovieUtils
)
if __name__ == "__main__":
    RequestApi.test()
    MovieUtils.get_movies(Genre.Scifi.value)
    # ArtistaUtils.get_artistas("Arnold")
