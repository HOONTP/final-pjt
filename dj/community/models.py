from django.db import models
from django.conf import settings
from django.utils import timezone
from common.models import BaseModel

class Board(models.Model):
    name = models.CharField(max_length=255)
    
class Article(BaseModel): # 이거 하나로 여러개의 게시판을 만들 수 있나?
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles'
    )
    is_active  = models.BooleanField(default=True)
    is_notice  = models.BooleanField(default=False)
    counting = models.PositiveIntegerField(default=0)  # 조회 수 필드 추가
    def increment_counting(self):
        self.counting += 1
        self.save()

    def save(self, *args, **kwargs):
        # 이전 데이터를 가져옵니다.
        try:
            old_data = Article.objects.get(pk=self.pk)
        except Article.DoesNotExist:
            # 새로운 데이터일 경우에는 기본 save 메서드를 호출하여 저장합니다.
            super(Article, self).save(*args, **kwargs)
            return

        # title이나 content가 변경되었을 때만 updated_at을 업데이트합니다.
        if self.title != old_data.title or self.content != old_data.content:
            self.updated_at = timezone.now()
        super(Article, self).save(*args, **kwargs)


class Comment(BaseModel):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_comments'
        )
    is_active  = models.BooleanField(default=True)


class Reply(BaseModel):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies'
        )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_replies'
        )
    is_active  = models.BooleanField(default=True)
