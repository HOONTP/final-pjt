from rest_framework import serializers
from .models import CustomUser
from movies.models import Movie, Review
from community.models import Article, Comment, Reply
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


#forms.py처럼 두개로 나눠서 해야될까 ??
class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    password = serializers.CharField(write_only=True)  # 패스워드는 쓰기 전용으로 설정
    password2 = serializers.CharField(write_only=True)
    like_articles = serializers.SerializerMethodField()
    like_comments = serializers.SerializerMethodField()
    like_replies = serializers.SerializerMethodField()
    like_movies = serializers.SerializerMethodField()
    like_Reviews = serializers.SerializerMethodField()
    user_articles = serializers.SerializerMethodField()
    user_comments = serializers.SerializerMethodField()
    user_replies = serializers.SerializerMethodField()
    user_Reviews = serializers.SerializerMethodField()
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ('followings',)

    def get_like_objects(self, user, model):
        # 해당 사용자가 좋아요한 객체 리스트를 반환하는 메소드
        return model.objects.filter(like_users=user)
    
    def get_user_objects(self, user, model):
        return model.objects.filter(user=user)

    def get_like_articles(self, user):
        return ArticleSerializer(self.get_like_objects(user, Article), many=True).data

    def get_like_comments(self, user):
        return CommentSerializer(self.get_like_objects(user, Comment), many=True).data

    def get_like_replies(self, user):
        return ReplySerializer(self.get_like_objects(user, Reply), many=True).data

    def get_like_movies(self, user):
        return MovieSerializer(self.get_like_objects(user, Movie), many=True).data

    def get_like_Reviews(self, user):
        return ReviewSerializer(self.get_like_objects(user, Review), many=True).data

    def get_user_articles(self, user):
        return ArticleSerializer(self.get_user_objects(user, Article), many=True).data

    def get_user_comments(self, user):
        return CommentSerializer(self.get_user_objects(user, Comment), many=True).data

    def get_user_replies(self, user):
        return ReplySerializer(self.get_user_objects(user, Reply), many=True).data

    def get_user_Reviews(self, user):
        return ReviewSerializer(self.get_user_objects(user, Review), many=True).data