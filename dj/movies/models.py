from django.db import models
from django.conf import settings
# from accounts.models import User
# Create your models here.
def articles_image_path(instance, filename):
	return f'images/{instance.user.username}/{filename}'


"""

    {
      "adult": false,
      "backdrop_path": null,
      "genre_ids": [
        99
      ],
      "id": 322772,
      "original_language": "en",
      "original_title": "Insane Fight Club II - This Time It’s Personal",
      "overview": "Insane Fight Club is back. This year the boys are taking their unique form of entertainment to England as they stage fight nights in Birmingham, Leeds, Liverpool and Newcastle.",
      "popularity": 2.348,
      "poster_path": null,
      "release_date": "2015-01-21",
      "title": "Insane Fight Club II - This Time It’s Personal",
      "video": false,
      "vote_average": 7,
      "vote_count": 2
    },
genre
    {
      "id": 28,
      "name": "Action"
    },
    {
"""
class Movie(models.Model):
    # genre_ids = models.CharField(max_length=10)
    id = models.IntegerField(primary_key=True)
    genre_ids = models.ManyToManyField("movies.Genre", related_name="genremovie")#통합조회시
    actor_ids = models.ManyToManyField("movies.Actor", related_name="actormovie")
    director = models.ForeignKey("movies.Director", on_delete=models.CASCADE, related_name="directormovie", blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    vote_average = models.FloatField(default=0, blank=True, null=True)
    title = models.CharField(max_length=10)
    overview = models.TextField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    # , blank=True, null=True
    # actors = models.ManyToManyField("movies.Actor", related_name="movies")
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # image = models.ImageField(blank=True, upload_to=articles_image_path)
    # image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')
    # movies = models.ManyToManyField("movies.Movie", related_name="actors") #Movie.acotrs.
    # created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
  
class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_Reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_Reviews')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


# class Actor(models.Model):
#     name = models.CharField(max_length=100)
