from django.urls import path
from . import views

urlpatterns = [
    path('kakaoLogin/', views.kakaoLogin, name='kakaoLogin'),
    path('verifyToken/', views.verifyToken, name='verifyToken'),
    path('account/<str:pk>/delete', views.deleteUser, name='delete_user'),
]
