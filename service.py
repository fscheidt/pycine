import json

class Service:

    @staticmethod
    def get_genres():
        genres = json.load(open('./data/genres.json'))
        return genres
