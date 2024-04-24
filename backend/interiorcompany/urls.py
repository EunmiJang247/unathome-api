from django.urls import path
from . import views

urlpatterns = [
    path('interiorcompany/', views.getAllInteriorcompany, name='interiorcompany'),
    path('interiorcompany/new/', views.newInteriorcompany, name='new_interiorcompany'),
]
