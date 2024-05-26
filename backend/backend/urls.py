from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('portfolio.urls')),
    path('api/', include('account.urls')),
    path('api/', include('customerreview.urls')),
    path('api/', include('interiorcompany.urls')),
    path('api/', include('story.urls')),
    path('api/', include('consultant.urls')),
    path('api/', include('faq.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = 'utils.error_views.handler500'
handler404 = 'utils.error_views.handler404'