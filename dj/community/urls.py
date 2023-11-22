from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('<int:community_pk>/articles/<int:user_pk>/', views.article), # 모든 게시글 조회 및 입력
    path('articles/<int:article_pk>/', views.article_detail), # 게시글 상세 조회
    path('comments/', views.comment_detail), #'GET' 내가 쓴 댓글 보기
    path('articles/<int:article_pk>/comments/', views.comment_detail), # 'POST'
    path('articles/<int:article_pk>/<int:comment_pk>/', views.comment_detail),#'DELETE','PUT'
    path('comments/<int:comment_pk>/replies/', views.reply_detail), # 'POST'
    path('comments/<int:comment_pk>/<int:reply_pk>/', views.reply_detail),#'DELETE','PUT'
    # 좋아요 기능
    path('like/article/<int:article_pk>/', views.like_article),
    path('like/comment/<int:comment_pk>/', views.like_comment),
    path('like/reply/<int:reply_pk>/', views.like_reply),
    # 검색
    path('search/<int:comment_pk>/', views.search_article), # GET 게시글 검색(제목 내용 닉네임)
    # 인기글
    path('hot/', views.hot_article),
]
