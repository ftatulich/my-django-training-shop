from django.conf.urls.static import static
from django.urls import path

from DjangoShop import settings
from .views import home_page, login_user_page, register_page, logout_user_page, product_info_page, categories_page, \
    category_page

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_user_page, name='login'),
    path('logout/', logout_user_page, name='logout'),
    path('register/', register_page, name='register'),
    path('products/<int:product_id>/', product_info_page, name='product'),
    path('categories/', categories_page, name='categories'),
    path('categories/<str:category_name>/', category_page, name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
