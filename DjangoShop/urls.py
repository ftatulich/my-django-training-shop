from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve

from DjangoShop import settings

urlpatterns = [
    path('', include('shop.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('wishlist/', include('wishlist.urls')),
    path('search/', include('search.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
]
