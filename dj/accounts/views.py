from django.shortcuts import render
import math

# Create your views here.

# from .models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from django.http import JsonResponse

from .serializers import UserSerializer, ProfileUpdateSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.authtoken.models import Token
from rest_framework.parsers import MultiPartParser, FormParser


class ProfileUpdateView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        serializer = ProfileUpdateSerializer(data=request.data)
        if serializer.is_valid():
            # 사용자 모델 업데이트
            request.user.profile_image = serializer.validated_data.get('profile_image', '')
            request.user.introduce = serializer.validated_data.get('bio', '')
            request.user.save()
            return Response({'message': 'Profile updated successfully'})
        else:
            return Response(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    if request.method == 'POST':
        bio = request.POST.get('bio', '')
        
        # 이미지 파일 처리
        profile_picture = request.FILES.get('profile_picture', None)
        if profile_picture:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.profile_picture = profile_picture
            user_profile.save()

        return JsonResponse({'message': '프로필이 업데이트되었습니다.'})
    else:
        return JsonResponse({'message': 'POST 요청만 허용됩니다.'})

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

