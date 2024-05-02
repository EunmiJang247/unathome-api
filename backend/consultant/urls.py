from django.urls import path
from . import views

urlpatterns = [
  path('consultant/my/', views.getMyConsultant, name='get_my_consultant'),
  path('consultant/new/', views.createConsultant, name='new_consultant'),
  path('consultant/<str:pk>/', views.readConsultant, name='get_consultant'),
]
