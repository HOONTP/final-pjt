from rest_framework import serializers
from .models import Movie, Review, Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)

    # like_count = serializers.IntegerField(source='liked_users.count', read_only=True) / , 'like_users'

class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer): # MovieSerializer로 이름을 위와 같게 지정해도 문제 없음
        class Meta:
            model = Movie
            fields = ('title',)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'like_users', 'uesr',)

'''
read_only_fields = ('movie',)
Reviews = ReviewSerializer(many=True, read_only=True)
두 read_only는 다름. ( 교차 사용 안댐 )
'''
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = ('name',)
    genres = GenreNameSerializer(many=True, read_only=True, source='genre_ids')
    # source로 참조될 데이터를 줘야 serializer할 때에 해당 필드에서 적합한 데이터를 가져옴.
    class Meta:
        model = Movie
        fields = '__all__'