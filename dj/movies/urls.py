from django.urls import path
from . import views

app_name = 'movies' # 'movies:---' 로 경로 호출 시 사용?
urlpatterns = [
    path('', views.movie_list),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/reviews/', views.create_review),
    path('<int:movie_pk>/likes/', views.add_user_to_movie_likes),
    path('recommend/', views.recommend_movie),
    path('reviews/', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('search/', views.search_movie),
    
    path('loadmovies/', views.get_movie_datas),
    path('loadgenres/', views.get_genre_datas),
    path('loadmoviedetail/', views.get_movie_detail),
]
