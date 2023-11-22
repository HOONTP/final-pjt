from rest_framework import serializers
from .models import Article, Comment, Reply

class ArticleListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

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
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user', 'like_users',)