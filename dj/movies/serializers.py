from rest_framework import serializers
from .models import Movie, Review, Genre, Actor

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True, read_only=True)
    # genres = GenreSerializer(many=True, read_only=True, source='genre_ids')
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)

    # like_count = serializers.IntegerField(source='liked_users.count', read_only=True) / , 'like_users'

class ReviewSerializer(serializers.ModelSerializer):
    # class MovieTitleSerializer(serializers.ModelSerializer): # MovieSerializer로 이름을 위와 같게 지정해도 문제 없음
    #     class Meta:
    #         model = Movie
    #         fields = ('title',)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    # movie_title = MovieTitleSerializer(read_only=True, source='movie')
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'like_users', 'user',)

class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True, source='movie_reviews')
    review_count = serializers.IntegerField(source='movie_reviews.count', read_only=True)
    genre_ids = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True, source='actor_ids')
    # source로 참조될 데이터를 줘야 serializer할 때에 해당 필드에서 적합한 데이터를 가져옴.
    class Meta:
        model = Movie
        fields = '__all__'