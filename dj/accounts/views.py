from django.shortcuts import render

# Create your views here.

# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404



@api_view(['POST'])
def user_create(request):
    User = get_user_model()

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 비밀번호를 해시로 설정
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data.get('email', ''),
                password=serializer.validated_data['password']
            )
            user.first_name = serializer.validated_data.get('first_name', '')
            user.last_name = serializer.validated_data.get('last_name', '')
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def person(request, user_pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'GET':
        serializer = UserSerializer(user, partial=True)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['POST', 'DELETE'])
def log(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            auth_login(request, serializer.get_user())
            return Response
    elif request.method == 'DELETE':
        auth_logout(request)


# @api_view(['GET'])
# def profile(request, user_pk):
#     User = get_user_model()
#     user = get_object_or_404(User, pk=user_pk)
#     serializer = UserSerializer(user, partial=True)
#     return Response(serializer.data)

@api_view(['POST'])
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
