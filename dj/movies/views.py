from django.shortcuts import render

# Create your views here.
from .models import Movie, Review, Genre, Actor, Director
from django.contrib.auth import get_user_model as User
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404

from django.conf import settings
import requests
from django.db import IntegrityError
from decouple import config

from django.utils.timezone import make_aware
from datetime import datetime


TMDB_API_KEY = config('TMDB_API_KEY')

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True, partial=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)       
        
    elif request.method == 'DELETE':
        # if movie.user == request.user:
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_list(request):
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        # if Review.user == request.user:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# 좋아요는 POST 기능,,

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_user_to_movie_likes(request, movie_pk, user_pk):
    # POST 요청의 본문에서 영화 ID와 사용자 ID를 가져옴
    # Postman에서 user정보를 어케하지
    try:
        movie = Movie.objects.get(pk=movie_pk)
        user = User.objects.get(pk=user_pk)
        # N:M 관계에 사용자를 추가
        if user in movie.like_users.all():
            movie.like_users.remove(user)
            return Response({'message': 'User removed to movie likes successfully.'})
        else:
            movie.like_users.add(user)
            return Response({'message': 'User added to movie likes successfully.'})
    except Movie.DoesNotExist:
        return Response({'message': 'Movie not found.'}, status=400)
    except User.DoesNotExist:
        return Response({'message': 'User not found.'}, status=400)
    
'''
def index(request):
    movie = get_list_or_404()
이런 식으로하면 게시글이 없을 때 페이지를 키면 => 404 에러가 되버림.
-> API를 개발할 때 사용하도록,,
'''




def get_movie_datas(request):
    # 1페이지부터 500페이지까지 (페이지당 20개, 총 10,000개)
    Movie.objects.all().delete()
    count = 0

    for i in range(1, 501):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()

        for movie in movies['results']:
            if movie['poster_path'] == 'null':
                movie['poster_path'] = 0
            if movie.get('release_date', ''):
                genre_ids = movie.get('genre_ids', [])#[]
                # movie_instance.genre_ids.set(genre_ids)
                release_date_str = movie.get('release_date', '')

                fields = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'release_date': make_aware(datetime.strptime(release_date_str, '%Y-%m-%d')) if release_date_str else None,
                    'popularity': movie['popularity'],
                    'vote_average': movie['vote_average'],
                    'overview': movie['overview'],
                    'poster_path': movie['poster_path'],
                    'original_title': movie['original_title'],
                }
                try:
                    movie_instance = Movie.objects.create(**fields)
                    movie_instance.genre_ids.set(genre_ids)
                except Exception as e:
                    # print(fields)
                    count += 1
                    print(e, movie['id'])
    print(count)
    return JsonResponse({'message': 'movie load'})

def get_genre_datas(request):
    # TMDB API의 장르 목록을 가져오기
    api_url = 'https://api.themoviedb.org/3/genre/movie/list'
    language = 'ko'

    # TMDB API 키는 보안 상의 이유로 환경 변수 등을 통해 안전하게 설정해야 합니다.

    # TMDB API에 GET 요청 보내기
    response = requests.get(api_url, params={'api_key': TMDB_API_KEY, 'language': language})

    # 응답을 JSON으로 변환하여 처리
    if response.status_code == 200:
        genres_data = response.json().get('genres', [])

        # 장르 데이터를 Genre 모델에 저장
        for genre_data in genres_data:
            genre, created = Genre.objects.get_or_create(
                id=genre_data['id'],
                defaults={'name': genre_data['name']}
            )

        return JsonResponse({'message': 'Genres saved to the database'})
    else:
        return JsonResponse({'error': 'Failed to fetch genres from TMDB API'}, status=500)

def get_movie_detail(request):
    movies = get_list_or_404(Movie)
    count = 0
    for mov in movies:
        print(mov.id)
        language = 'ko-KR'
        api_url = f'https://api.themoviedb.org/3/movie/{mov.id}'
        movie = requests.get(api_url, params={'api_key': TMDB_API_KEY, 'language': language, 'append_to_response': 'credits'}).json()
        # print(movie)
        # mov = get_object_or_404(Movie, pk=mov.id)
        try:
            mov.runtime = movie['runtime']
            actors_id = []
            for i in range(len(movie['credits']['cast'])):
                actors_id.append(movie['credits']['cast'][i]['id'])
                actor, created = Actor.objects.get_or_create(
                    id=movie['credits']['cast'][i]['id'],
                    defaults={'name': movie['credits']['cast'][i]['name']}
                )
                if i == 10:
                    break
            mov.actor_ids.set(actors_id)
            
            for i in range(len(movie['credits']['crew'])):
                if movie['credits']['crew'][i]['known_for_department'] == "Directing":
                    director, created = Director.objects.get_or_create(
                    id=movie['credits']['crew'][i]['id'],
                    defaults={'name': movie['credits']['crew'][i]['name']}
                    )
                    direct = get_object_or_404(Director, pk=movie['credits']['crew'][i]['id'])
                    mov.director = direct
                    break
            mov.save()
        except Exception as e:
            print(e)
            count += 1
    print(count)
    return JsonResponse({'message': 'people load'})






# @api_view(['GET'])
# def actor_list(request):
#     actors = get_list_or_404(Actor)
#     # actors = Actor.objects.all()
#     serializer = ActorSerializer(actors, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def actor_detail(request, actor_pk):
#     actor = get_object_or_404(Actor, pk=actor_pk)
#     serializer = ActorSerializer(actor)
#     return Response(serializer.data)