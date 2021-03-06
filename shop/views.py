

from django.contrib.auth.models import Permission
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from .forms.profile_forms import ChangePermissionsForm
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
    messages.success(request, 'Ви вийшлі з облікового запису')
    return redirect('login')


def product_info_page(request, product_id: int):
    """В'юшка для окремого товару"""
    context = generate_product_page(product_id, request)
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
    if username == request.user.username:
        products = get_products_by_seller(username)
        return render(request, 'shop/my_profile.html', {'products': products})
    else:
        products = get_approved_products_by_seller(username)
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
        return edit_profile_post(request)
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
        return save_edit_product_changes(request, product)

    form = EditProductForm(instance=product)
    return render(request, 'shop/edit_product.html', {'form': form})


@login_required
def delete_product(request, product_id: int):
    """Видаляє пост"""
    product = get_product_by_id(product_id)

    if request.user.has_perm('change_product') or product.seller == request.user:
        send_mail(
            subject='Ваш товар було видалено',
            message='Ви видалили ваш товар, або його було видалено з нашої платформи за порушення правил',
            recipient_list=[product.seller.email],
            from_email='kartieltv@gmail.com',
        )

        product.delete()
        messages.success(request, "Товар було видалено")
        return redirect('home')
    else:
        messages.error(request, "У вас немає необхідних прав.")
        return redirect('home')


@login_required
def change_permissions(request, user_id: int):
    if request.user.has_perm('auth.change_permission') and request.user.id != user_id:
        user = get_object_or_404(CustomUser, pk=user_id)

        if request.method == "POST":
            form = ChangePermissionsForm(request.POST)

            if form.is_valid():
                form_permissions = form.cleaned_data.get('permissions')
                permissions = Permission.objects.filter(codename__in=form_permissions)
                user.user_permissions.set(permissions)

                messages.success(request, 'Права Успішно додані')
                return redirect(reverse('change_permission', args=[user_id]))
            else:
                messages.error(request, 'Змініть права')
                return redirect(reverse('change_permission', args=[user_id]))
        else:
            permissions = []
            for perm in user.user_permissions.all():
                permissions.append(perm.codename)

            form = ChangePermissionsForm(initial={
                'permissions': permissions
            })

            return render(request, 'shop/change_permissions.html', {'form': form, 'user': user})
    else:
        messages.error(request, 'У вас немає прав для цієї дії')
        return redirect('home')


@login_required
def moderation(request):
    context = dict()
    if request.user.has_perm('add_product'):
        context.update({
            'products': Product.objects.filter(approved=False)
        })

    return render(request, 'shop/moderation.html', context)


@login_required
def approve(request, product_id: int):
    if request.user.has_perm('change_product'):
        product = get_product_by_id(product_id)
        product.approved = True
        product.save()
        return redirect(reverse('product', args=[product_id]))
    else:
        messages.error(request, 'Ви не маєте необхідних прав.')
        return redirect('home')

