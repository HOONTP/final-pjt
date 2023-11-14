from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/', views.detail, name='detail'),
    path(
        '<int:review_pk>/comments/create/',
        views.create_comment,
        name='create_comment',
    ),
    path('<int:review_pk>/like/', views.like, name='like'),

    
    path('api/v1/articles/', views.article), # 모든 게시글 조회 및 입력
    path('api/v1/articles/<int:article_pk>/', views.article_detail), # 게시글 상세 조회
    path('api/v1/comments/', views.comment_detail), #'GET' 내가 쓴 댓글 보기
    path('api/v1/articles/<int:article_pk>/comments/', views.comment_detail), # 'POST'
    path('api/v1/articles/<int:article_pk>/<int:comment_pk>/', views.comment_detail),#'DELETE','PUT'

    path('<int:movie_pk>/likes/<int:user_pk>/', views.add_user_to_movie_likes),


]
