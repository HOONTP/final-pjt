from django.urls import path
from . import views

app_name = 'movies' # 'movies:---' 로 경로 호출 시 사용?
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    
    path('api/v1/movies/', views.movie_list),
    path('api/v1/movies/<int:movie_pk>/', views.movie_detail),
    path('api/v1/reviews/', views.review_list),
    path('api/v1/reviews/<int:review_pk>/', views.review_detail),
    path('api/v1/movies/<int:movie_pk>/reviews/', views.create_review),

    path('<int:movie_pk>/likes/<int:user_pk>/', views.add_user_to_movie_likes),
    # path('api/v1/actors/', views.actor_list),
    # path('api/v1/actors/<int:actor_pk>/', views.actor_detail),
]
