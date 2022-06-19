from django.urls import path

from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.card_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove')
]
