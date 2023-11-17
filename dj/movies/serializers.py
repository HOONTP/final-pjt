from rest_framework import serializers
from .models import Movie, Review, Genre

# class ActorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Actor
#         fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    genre_ids = GenreSerializer(many=True)
    class Meta:
        model = Movie
        # fields = ('id', 'title', 'overview', 'like_users',)
        fields = '__all__'
        read_only_fields = ('like_users',)
        # exclude = ('genres',)

    # like_count = serializers.IntegerField(source='liked_users.count', read_only=True) / , 'like_users'

class ReviewSerializer(serializers.ModelSerializer):
    class MovieTitleSerializer(serializers.ModelSerializer): # MovieSerializer로 이름을 위와 같게 지정해도 문제 없음
        class Meta:
            model = Movie
            fields = ('title',)

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
    # movie 하나의 객체를 파라미터로 받기 때문에 그 객체의 코멘트가 참조된다. 어떻게 참조하는지는 모르겠음.
    # actors = ActorSerializer(many=True, read_only=True)
    #
    reviews = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='reviews.count', read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ('genre_ids')

