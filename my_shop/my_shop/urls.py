from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import main, contacts
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('products/', include('mainapp.urls', namespace='products')),
    path('auth/', include('authapp.urls', namespace='auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)