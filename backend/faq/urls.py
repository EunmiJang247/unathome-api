from . import views
from rest_framework.routers import DefaultRouter
from django.urls import (
    path,
    include,
)

app_name = 'faq'
router = DefaultRouter()
router.register('faq', views.FaqViewSet, basename='faq_tags')

urlpatterns = [
    path('', include(router.urls))
]
