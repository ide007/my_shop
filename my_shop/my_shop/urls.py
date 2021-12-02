from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import main, contacts
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('', include('social_django.urls', namespace='social')),
    path('contacts/', contacts, name='contacts'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('products/', include('mainapp.urls', namespace='products')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('orders/', include('ordersapp.urls', namespace='orders')),
    path('admin_staff/', include('adminapp.urls', namespace='admin_staff')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar
    import mimetypes

    mimetypes.add_type("application/javascript", ".js", True)

    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

    urlpatterns = [path('__debug__/',
                        include(debug_toolbar.urls)), ] + urlpatterns