from django.shortcuts import render
import math

# Create your views here.

# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.http import JsonResponse

from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.authtoken.models import Token
from movies.models import Movie, Director, Genre
from movies.serializers import MovieListSerializer

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@authentication_classes([])
def person(request, user_pk=-1):
    User = get_user_model()
    print(user_pk)
    if user_pk != -1:
        user = get_object_or_404(User, pk=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user, partial=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('b')
            # 비밀번호를 해시로 설정
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email', ''),
                password=serializer.validated_data['password'],
                nickname=serializer.validated_data['nickname']
                
            )
            print(user)
            user.first_name = serializer.validated_data.get('first_name', '')
            user.last_name = serializer.validated_data.get('last_name', '')
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors) 
    elif request.method == 'DELETE':
        if user == request.user:
            user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        if user == request.user:
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

@api_view(['POST', 'DELETE'])
@authentication_classes([])
def log(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = None
            
            return Response({
                'token': token.key if token else None,
                'user_id': user.id,
                'username': user.username,
                'email': user.email,
            })
        else:
            # 사용자 인증 실패 시 에러 응답
            return JsonResponse({'message': 'Invalid credentials'}, status=400)

    elif request.method == 'DELETE':
        auth_logout(request)
        return JsonResponse({'message': 'logout success'})


# @api_view(['GET'])
# def profile(request, user_pk):
#     User = get_user_model()
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = UserSerializer(user, partial=True)
#     return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        # if request.user in person.followers.all():
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            return Response({'message': 'follow success'})
        else:
            person.followers.add(request.user)
            return Response({'message': 'unfollow success'})

@api_view(['GET'])
@authentication_classes([])
def recommend_movie(request):#like_movies
    User = get_user_model()
    user = get_object_or_404(User, pk=1)
    like_movies = user.like_movies.all()
    GR = get_list_or_404(Genre)
    movies = get_list_or_404(Movie)
    genres = {}
    for G in GR:
        genres[G.id] = 0
    if len(like_movies) >= 5:
        directors = set()
        for movie in like_movies:
            directors.add(get_object_or_404(Director, pk=movie.director_id))
            movie_genres = movie.genre_ids.all()
            for genre in movie_genres:
                genres[genre.id] += 1
        value_lst = []
        for movie in movies:
            genre_value = 0
            if movie.director in directors and movie not in like_movies:
                for genre, value in genres.items():
                    cal_value = math.log(3+value) * 10
                    # if get_object_or_404(Genre, pk=genre) in movie.genre_ids.all() and genre_value < cal_value:
                    if movie.genre_ids.filter(pk=genre).exists() and genre_value < cal_value:
                        print(cal_value)
                        genre_value = cal_value
            sums_value = min(genre_value, 50) + movie.popularity + (movie.vote_average * 5)
            value_lst.append([sums_value, movie])
        sorted_list = sorted(value_lst, key=lambda x: x[0], reverse=True)
        show_lst = []
        cnt = 0
        print(sorted_list)
        for getMovie in sorted_list:
            show_lst.append(getMovie[1])
            cnt += 1
            if cnt >= 5:
                break
        serializer = MovieListSerializer(show_lst, many=True, partial=True)
        return Response(serializer.data)
    else:
        return JsonResponse({'message':'관심 영화가 5개 이상 필요합니다.'})