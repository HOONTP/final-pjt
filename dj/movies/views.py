from django.shortcuts import render

# Create your views here.
from .models import Movie, Review
from django.contrib.auth import get_user_model as User
from .serializers import MovieListSerializer, MovieSerializer, ReviewSerializer


from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404, get_list_or_404


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        # movies = Movie.objects.all()
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True, partial=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
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
def review_list(request):
    # Reviews = Review.objects.all()
    reviews = get_list_or_404(Review)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # Review = Review.objects.get(pk=Review_pk)
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
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# 좋아요는 POST 기능,,

@api_view(['POST'])
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