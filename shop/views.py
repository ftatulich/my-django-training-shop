from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import AddProductForm
from .models import Product, Category
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


def categories_page(request):
    """Показує всі категорії"""
    categories = Category.objects.all()
    return render(request, 'shop/allcategories.html', {'categories': categories})


def seller_profile(request, username):
    """Сторінка адміністрування продавця"""
    products = Product.objects.filter(seller__username=username).select_related('category')
    if username == request.user.username:
        return render(request, 'shop/my_profile.html', {'products': products})
    else:
        return render(request, 'shop/profile.html', {'username': username, 'products': products})


@login_required
def add_product(request):
    """Додавання товару"""
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect(reverse('product', args=[product.pk]))
        else:
            return render(request, 'shop/add_post.html', {'form': form})
    else:
        form = AddProductForm()
        return render(request, 'shop/add_post.html', {'form': form})
