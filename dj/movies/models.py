from django.db import models
from django.conf import settings
# from accounts.models import User
# Create your models here.
def articles_image_path(instance, filename):
	return f'images/{instance.user.username}/{filename}'

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre_ids = models.ManyToManyField("movies.Genre", related_name="genremovie")#통합조회시
    actor_ids = models.ManyToManyField("movies.Actor", related_name="actormovie")
    director = models.ForeignKey("movies.Director", on_delete=models.CASCADE, related_name="directormovie", blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    vote_average = models.FloatField(default=0, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    original_title = models.CharField(max_length=100, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    popularity = models.IntegerField(blank=True, null=True)
    release_date = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    poster_path = models.TextField(blank=True, null=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')

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
