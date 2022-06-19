from django.urls import path
from .views import wishlist, add_wishlist, remove_wishlist, clear_wishlist


urlpatterns = [
    path('', wishlist, name='wishlist'),
    path('add/', add_wishlist, name='add_wishlist'),
    path('remove/', remove_wishlist, name='remove_wishlist'),
    path('clear/', clear_wishlist, name='clear_wishlist'),
]
