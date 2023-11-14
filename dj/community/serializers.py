from rest_framework import serializers
from .models import Article, Comment

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['article', 'user']
