from . import views
from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

app_name = 'portfolio'
router = DefaultRouter()
router.register('tags', views.TagViewSet, basename='portfolios_tags')
router.register('portfoliolike', views.PortpolioLikeViewSet, basename='portfolios_likes')

urlpatterns = [
    path('portfolios/', views.getAllPortfolio, name='portfolios'),
    path('portfolios/main/', views.getMainPagePortfolio, name='main_portfolios'),
    path('portfolios/keywords/', views.getMainPageKeywordsPortfolio, name='keywords_portfolios'),
    path('portfolios/new/', views.newPortfolio, name='new_portfolios'),
    path('portfolios/mylikes/', views.myLikePortfolios, name='new_portfolios'),
    path('portfolios/<str:pk>/mylikeornot/', views.myLikeOrNot, name='mylike_portfolio'),
    path('portfolios/<str:pk>/', views.getPortfolio, name='portfolio'),
    path('portfolios/<str:pk>/update/', views.updatePortfolio, name='update_portfolio'),
    path('portfolios/<str:pk>/delete/', views.deletePortfolio, name='delete_portfolio'),
    path('portfolios/<str:pk>/like/', views.likePortfolio, name='like_portfolio'),
    path('', include(router.urls))
]
