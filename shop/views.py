from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .forms.product_forms import EditProductForm

from .services.main_services import *
from .services.login_sevices import *
from .services.register_services import *
from .services.profile_services import *
from .services.product_services import *


def home_page(request):
    """"Головна сторінка, популярні та недавні товарі, деякі категоріїї"""
    context = home_page_logic(request)
    return render(request, 'shop/index.html', context)


def login_user_page(request):
    """Авторизація користовуча"""
    return login_user_validate(request)


def register_page(request):
    """Реєстрація користувача"""
    return validate_register(request)


def logout_user_page(request):
    """Вихід з системи"""
    logout(request)
    return redirect('login')


def product_info_page(request, product_id: int):
    """В'юшка для окремого товару"""
    context = generate_product_page(product_id)
    return render(request, 'shop/product.html', context)


def category_page(request, category_name: str):
    """В'юшка для показу всіх товарів окремої категорії"""
    context = generate_category_page(category_name)
    return render(request, 'shop/products.html', context)


def categories_page(request):
    """Показує всі категорії"""
    categories = Category.objects.all()
    return render(request, 'shop/allcategories.html', {'categories': categories})


def seller_profile(request, username):
    """Сторінка адміністрування продавця"""
    products = get_products_by_seller(username)
    if username == request.user.username:
        return render(request, 'shop/my_profile.html', {'products': products})
    else:
        return render(request, 'shop/profile.html', {'username': username, 'products': products})


@login_required
def add_product(request):
    """Додавання товару"""
    if request.method == 'POST':
        return add_product_post(request)
    else:
        form = AddProductForm()
        return render(request, 'shop/add_post.html', {'form': form})


@login_required
def edit_profile(request):
    """Сторінка редагування профілю"""
    if request.method == 'POST':
        return edit_profile(request)
    else:
        form = EditProfileForm(instance=request.user)
        return render(request, 'shop/edit_profile.html', {'form': form})


@login_required
def edit_product(request, product_id: int):
    """Редагує пост"""
    product = get_product_by_id(product_id)
    if product.seller != request.user:
        return redirect('home')
    if request.method == 'POST':
        return save_product_changes_if_form_valid(request, product)
    form = EditProductForm(instance=product)
    return render(request, 'shop/edit_product.html', {'form': form})


@login_required
def delete_product(request, product_id: int):
    """Видаляє пост"""
    product = get_product_by_id(product_id)
    if product.seller != request.user:
        return redirect('home')

    product.delete()
    return redirect('home')
