from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/login/refresh/', TokenRefreshView.as_view()),
    path('api/chatbot/', include('chatbot.urls')),
]

from django.views.static import serve
from django.urls import re_path

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]