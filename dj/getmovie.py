import requests
from movies.models import Movie
from django.db import IntegrityError
from decouple import config


TMDB_API_KEY = config('TMDB_API_KEY')

def get_movie_datas():
    total_data = []

    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie.get('release_date', ''):
                genres_ids = movie.get('genre_ids', [])
                fields = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'released_date': movie['release_date'],
                    # 'popularity': movie['popularity'],
                    'vote_avg': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'genres_ids': genres_ids,
                }
                # Attempt to create a Movie instance and save it to the database
                try:
                    movie_instance = Movie.objects.create(**fields)
                except IntegrityError:
                    # Handle the case where a movie with the same movie_id already exists
                    movie_instance = Movie.objects.get(id=fields['id'])
                    # Update the fields if needed
                    movie_instance.title = fields['title']
                    movie_instance.released_date = fields['released_date']
                    movie_instance.vote_avg = fields['vote_avg']
                    movie_instance.poster_path = fields['poster_path']
                    movie_instance.genres_ids = genres_ids
                    movie_instance.save()

get_movie_datas()