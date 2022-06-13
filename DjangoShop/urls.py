from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
