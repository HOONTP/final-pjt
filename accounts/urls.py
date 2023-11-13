from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('<int:user_pk>/person/', views.person),
    path('user/create/', views.user_create),
    path('log/', views.log),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
