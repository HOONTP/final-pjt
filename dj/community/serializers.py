from rest_framework import serializers
from .models import Article, Comment, Reply

class ArticleListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    comment_reply_count = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_title(self, obj):
        # is_notice가 True이면 "공지 "를 추가한 제목을 반환, 아니면 기존 제목을 반환
        return f"[공지] {obj.title}" if obj.is_notice else obj.title
    def get_comment_reply_count(self, obj):
        # obj는 현재 직렬화하고 있는 Article 인스턴스입니다.
        comment_count = obj.comments.filter(is_active=True).count()
        reply_count = Reply.objects.filter(comment__article=obj, is_active=True).count()
        return comment_count + reply_count

class ReplySerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    # class ArticleGetSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = 
    article = serializers.PrimaryKeyRelatedField(source='comment.article', read_only=True)
    class Meta:
        model = Reply
        fields = '__all__'
        read_only_fields = ('user', 'comment', 'like_users',)

class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    replies = ReplySerializer(many=True, read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'article', 'like_users',)

class ArticleSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, required=False) # 관계모델에서 related값과 동일하게
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    profile_image = serializers.CharField(source='user.profile_image', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)