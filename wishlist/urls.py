from django.urls import path
from .views import wishlist_page, add_wishlist, remove_wishlist, clear_wishlist


urlpatterns = [
    path('', wishlist_page, name='wishlist'),
    path('add/<int:product_id>/', add_wishlist, name='add_wishlist'),
    path('remove/<int:product_id>/', remove_wishlist, name='remove_wishlist'),
    path('clear/', clear_wishlist, name='clear_wishlist'),
]
