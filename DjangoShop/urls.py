from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
