from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token

# Create your models here.
class CustomUser(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=255, unique=True)
    introduce = models.CharField(max_length=100, null=True, blank=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # 사용자 저장 시 토큰 생성
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)