from django.urls import path
from . import views

urlpatterns = [
  path('consultant/new/', views.createConsultant, name='new_consultant'),
]
