from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.authtoken.models import Token
from PIL import Image, ImageSequence
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)  # 자동으로 증가하는 기본 키 설정
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    nickname = models.CharField(max_length=255, unique=True)
    introduce = models.CharField(max_length=100, null=True, blank=True)
    # image = models.ImageField(upload_to='images/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def save(self, *args, **kwargs):
        # 사용자 저장 시 토큰 생성
        super().save(*args, **kwargs)
        Token.objects.get_or_create(user=self)
        if self.profile_image and self.profile_image.name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # 원하는 크기로 이미지를 조절
            max_width = 300
            max_height = 300
            image = Image.open(self.profile_image.path)
            if image.width > max_width or image.height > max_height:
                # 이미지가 설정한 최대 크기를 초과하는 경우 리사이징
                new_size = (max_width, max_height)

                # GIF 파일의 경우 모든 프레임에 대해 처리
                if hasattr(image, 'is_animated') and image.is_animated:
                    frames = [frame.copy() for frame in ImageSequence.Iterator(image)]
                    for i, frame in enumerate(frames):
                        frame.thumbnail(new_size)
                        frames[i] = frame

                    # 모든 프레임을 병합하여 다시 저장
                    frames[0].save(
                        self.profile_image.path,
                        save_all=True,
                        append_images=frames[1:],
                        loop=0
                    )
                else:
                    # 정적 이미지인 경우
                    image.thumbnail(new_size)
                    with BytesIO() as buffer:
                        image.save(buffer, format="JPEG")
                        buffer.seek(0)
                        self.profile_image.save(self.profile_image.name, ContentFile(buffer.read()), save=False)