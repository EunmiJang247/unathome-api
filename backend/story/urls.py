from django.urls import path
from . import views

urlpatterns = [
    path('story/', views.getAllStory, name='story'),
]
