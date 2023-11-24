from rest_framework import serializers
from .models import CustomUser
from movies.models import Movie, Review
from community.models import Article, Comment, Reply
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.conf import settings

class ProfileUpdateSerializer(serializers.Serializer):
    profile_image = serializers.ImageField(required=False)
    bio = serializers.CharField(required=False)  # 자기소개 필드 추가


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'password2', 'nickname', 'introduce', 'profile_image']

    def validate(self, data):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError("비밀번호와 비밀번호 확인이 일치하지 않습니다.")
        return data

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            nickname=validated_data['nickname'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    article = serializers.PrimaryKeyRelatedField(source='comment.article', read_only=True)
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
    user = get_user_model()
    like_articles = serializers.SerializerMethodField()
    like_comments = serializers.SerializerMethodField()
    like_replies = serializers.SerializerMethodField()
    like_movies = serializers.SerializerMethodField()
    like_reviews = serializers.SerializerMethodField()
    user_articles = serializers.SerializerMethodField()
    user_comments = serializers.SerializerMethodField()
    user_replies = serializers.SerializerMethodField()
    user_reviews = serializers.SerializerMethodField()
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='followings')
    
    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ('followings',)

    def get_like_objects(self, user, model):
        # 해당 사용자가 좋아요한 객체 리스트를 반환하는 메소드
        return model.objects.filter(like_users=user)

    def get_user_objects(self, user, model):
        return model.objects.filter(user=user).order_by('-created_at')

    def get_like_articles(self, user):
        return ArticleSerializer(self.get_like_objects(user, Article), many=True).data

    def get_like_comments(self, user):
        return CommentSerializer(self.get_like_objects(user, Comment), many=True).data

    def get_like_replies(self, user):
        return ReplySerializer(self.get_like_objects(user, Reply), many=True).data

    def get_like_movies(self, user):
        return MovieSerializer(self.get_like_objects(user, Movie), many=True).data

    def get_like_reviews(self, user):
        return ReviewSerializer(self.get_like_objects(user, Review), many=True).data

    def get_user_articles(self, user):
        return ArticleSerializer(self.get_user_objects(user, Article), many=True).data

    def get_user_comments(self, user):
        return CommentSerializer(self.get_user_objects(user, Comment), many=True).data

    def get_user_replies(self, user):
        return ReplySerializer(self.get_user_objects(user, Reply), many=True).data

    def get_user_reviews(self, user):
        return ReviewSerializer(self.get_user_objects(user, Review), many=True).data