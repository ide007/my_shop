from django.contrib import admin
from django.urls import path, include
from .views import main, contacts


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),
    path('contacts/', contacts),
    path('products/', include('mainapp.urls')),

]
