from django.urls import path
from . import views

urlpatterns = [
    path('customerreview/', views.getAllCustomerReview, name='customer_review'),
    path('customerreview/my/', views.getMyCustomerReview, name='customer_review'),
    path('customerreview/main/', views.getMainPageCustomerReview, name='main_customer_review'),
    path('customerreview/new/', views.newCustomerReview, name='new_customer_review'),
    path('customerreview/<str:pk>/', views.getCustomerReview, name='detail_customer_review'),
    path('customerreview/<str:pk>/update/', views.updateCustomerReview, name='update_customer_review'),
    path('customerreview/<str:pk>/delete/', views.deleteCustomerReview, name='delete_customer_review'),
]
