import requests
from tmdb.models import TMDBMovie, Genre

key = 'd1da20fbfa65312b857fb7b517bf855c'

class RequestApi:
    """
    
    Esta classe faz request para a API do tmdb,
    de acordo com funções pre-definidas do nosso app

    """
    @staticmethod
    def test():
        print('[ok] from RequestApi')

    @staticmethod
    def get_movie_popular_by_genre(genre: int):
        endpoint = f'https://api.themoviedb.org/3/discover/movie/?api_key={key}&certification_country=US&certification=R&sort_by=vote_count.desc&with_genres={genre}'
        r = requests.get(endpoint)
        # print(r.status_code) # deve retornar 200
        data = r.json()
        results = data['results']
        return results

    @staticmethod
    def get_artista(person_id):
        endpoint = f'https://api.themoviedb.org/3/person/{person_id}?api_key={key}'
        r = requests.get(endpoint)
        # print(r.status_code) # deve retornar 200
        data = r.json()
        results = data['results']
        return results


class MovieUtils:

    @staticmethod
    def get_movies(genre: int = 18):
        # obter o titulo (original_title)
        # percorremos a lista de filmes (results)

        results = RequestApi.get_movie_popular_by_genre(genre)
        for movie in results:
            m = TMDBMovie(
                movie['id'],
                movie['original_title'],
            )
            # title = movie['original_title']
            print(m.title, m.id)
        print(f'Filmes encontrados: {len(results)}')
