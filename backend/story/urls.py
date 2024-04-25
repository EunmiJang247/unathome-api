from django.urls import path
from . import views

urlpatterns = [
    path('story/', views.getAllStory, name='story'),
    path('story/new/', views.newStoryFunc, name='new_story'),
    path('story/<str:pk>/', views.getStory, name='detail_story'),
]
