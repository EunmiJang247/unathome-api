from django.urls import path
from . import views

urlpatterns = [
    path('portfolios/', views.getAllPortfolio, name='portfolios'),
    path('portfolios/main/', views.getMainPagePortfolio, name='main_portfolios'),
    path('portfolios/new/', views.newPortfolio, name='new_portfolios'),
    path('portfolios/<str:pk>/', views.getPortfolio, name='portfolio'),
    path('portfolios/<str:pk>/update/', views.updatePortfolio, name='update_portfolio'),
    path('portfolios/<str:pk>/delete/', views.deletePortfolio, name='delete_portfolio'),
]
