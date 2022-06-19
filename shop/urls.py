from django.conf.urls.static import static
from django.urls import path

from DjangoShop import settings
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_user_page, name='login'),
    path('logout/', logout_user_page, name='logout'),
    path('register/', register_page, name='register'),
    path('products/<int:product_id>/', product_info_page, name='product'),
    path('products/<int:product_id>/delete', delete_product, name='delete_product'),
    path('products/<int:product_id>/edit', edit_product, name='edit_product'),
    path('categories/', categories_page, name='categories'),
    path('categories/<str:category_name>/', category_page, name='category'),
    path('profile/<str:username>', seller_profile, name='profile'),
    path('addproduct/', add_product, name='add_product'),
    path('editprofile/', edit_profile, name='edit_profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
