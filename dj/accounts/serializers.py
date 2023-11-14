from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm

#forms.py처럼 두개로 나눠서 해야될까 ??
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # 패스워드는 쓰기 전용으로 설정

    class Meta:
        model = get_user_model()
        fields = '__all__'
        # exclude = ('')
        read_only_fields = ('followings',)