from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_pk>/person/', views.person), # 조회 수정 탈퇴
    path('user/', views.person), # 회원가입
    path('log/', views.log), # 로그인 로그아웃
    # path('profile/<int:user_pk>/', views.profile), # 유저 개별 프로필 person으로 되나
    path('<int:user_pk>/follow/', views.follow), # 팔로우 언팔로우
]
