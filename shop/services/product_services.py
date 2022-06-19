from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from shop.forms.product_forms import AddProductForm, EditProductForm
from shop.models import Product


def generate_product_page(product_id: int) -> dict:
    """Бере з БД інфу для продукту, і рендерить шаблон для сторінки цього продукту"""
    product = get_product_by_id(product_id)
    try:
        related_products = Product.objects.select_related('category').all().order_by('date')[:10]
    except Product.DoesNotExist:
        raise Http404('No %s matches the given query.')

    context = {
        'product': product,
        'related_products': related_products,
    }

    return context


def add_product_post(request):
    form = AddProductForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.seller = request.user
        product.save()
        return redirect(reverse('product', args=[product.pk]))
    else:
        return render(request, 'shop/add_post.html', {'form': form})


def get_products_by_seller(username: str) -> Product:
    products = Product.objects.filter(seller__username=username).select_related('category')

    return products


def get_product_by_id(id: int) -> Product:
    return get_object_or_404(Product.objects.select_related('category', 'seller'), pk=id)


def save_product_changes_if_form_valid(request, product):
    form = EditProductForm(request.POST, instance=product)
    if form.is_valid():
        form.save()
        return redirect(reverse('product', args=[product.pk]))
    return render(request, 'shop/edit_product.html', {'form': form})

