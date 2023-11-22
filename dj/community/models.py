from django.db import models
from django.conf import settings
from django.utils import timezone

class Board(models.Model):
    name = models.CharField(max_length=255)
    
class Article(models.Model): # 이거 하나로 여러개의 게시판을 만들 수 있나?
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


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_comments'
        )


class Reply(models.Model):
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