from django.http import Http404
from django.shortcuts import get_object_or_404

from shop.models import Product, Category


def generate_product_page(product_id: int) -> dict:
    """Бере з БД інфу для продукту, і рендерить шаблон для сторінки цього продукту"""
    product = get_object_or_404(Product.objects.select_related('category', 'seller').prefetch_related('images'), pk=product_id)
    try:
        related_products = Product.objects.select_related('category').all().order_by('date')[:10]
    except Product.DoesNotExist:
        raise Http404('No %s matches the given query.')

    context = {
        'product': product,
        'related_products': related_products,
    }

    return context


def generate_category_page(category_name: str) -> dict:
    """Повертає інфу всіх товарів деякої категорії"""
    try:
        products = Product.objects.filter(category__name=category_name).prefetch_related('images')
    except Product.DoesNotExist:
        raise Http404('No %s matches the given query.')

    context = {
        'category': category_name,
        'products': products,
    }

    return context


def home_page_logic(request) -> dict:
    """Бере з БД, категорії, недавні та популярні продукти, рендерить html"""
    categories = Category.objects.all()[:3]
    active_category = request.GET.get('activecategory') or "Ноутбуки"
    top_sell_category = request.GET.get('topsellcategory') or "Ноутбуки"

    try:
        recently_products = Product.objects.select_related('category').filter(category__name=active_category).order_by(
            'date')
        top_sell_products = Product.objects.select_related('category').filter(
            category__name=top_sell_category).order_by('-date')

    except Product.DoesNotExist:
        raise Http404('No %s matches the given query.')

    context = {
        'active_category': active_category,
        'top_sell_category': top_sell_category,
        'categories': categories,
        'recently_products': recently_products,
        'top_sell_products': top_sell_products,
    }

    return context
