from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop.models import Product


@require_POST
def card_add(request, product_id: int):
    """Додає товар у кошик"""
    cart = Cart(request)
    product = get_object_or_404(Product.objects.select_related('category'), id=product_id)

    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleand_form_data = form.cleaned_data
        cart.add(product=product,
                 quantity=cleand_form_data['quantity'],
                 update_quantity=cleand_form_data['update']
                 )

    return redirect(request.META.get('HTTP_REFERER') )


def cart_remove(request, product_id: int):
    """Видаляє продукт з кошику"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect(request.META.get('HTTP_REFERER')
                    )


def cart_detail(request):
    """Сторінка з товарами кошику"""
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
