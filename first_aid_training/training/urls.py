from django.urls import path
from . import views

urlpatterns = [
    path('', views.modules, name='modules'),
    path('scenarios/', views.scenarios, name='scenarios'),
    path('achievements/', views.achievements, name='achievements'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('profile/', views.profile, name='profile'),
]
