from django.contrib.auth import logout
from django.shortcuts import render, redirect

from .services import login_sevices, register_services, main_services


def home_page(request):
    """"Головна сторінка, популярні та недавні товарі, деякі категоріїї"""
    context = main_services.home_page_logic(request)
    return render(request, 'shop/index.html', context)


def login_user_page(request):
    """Авторизація користовуча"""
    return login_sevices.login_user_validate(request)


def register_page(request):
    """Реєстрація користувача"""
    return register_services.validate_register(request)


def logout_user_page(request):
    """Вихід з системи"""
    logout(request)
    return redirect('login')


def product_info_page(request, product_id: int):
    """В'юшка для окремого товару"""
    context = main_services.generate_product_page(product_id)
    return render(request, 'shop/product.html', context)


def category_page(request, category_name: str):
    """В'юшка для показу всіх товарів окремої категорії"""
    context = main_services.generate_category_page(category_name)
    return render(request, 'shop/products.html', context)
