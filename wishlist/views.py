from django.shortcuts import render, redirect
from .wishlist import Wishlist


def wishlist_page(request):
    """Показує всі товари за якими слідкує користувач"""
    print(dict(request.session))
    return render(request, 'wishlist/wishlist.html')


def add_wishlist(request, product_id: int):
    wishlist = Wishlist(request)
    wishlist.add(product_id)

    return redirect(request.META.get('HTTP_REFERER'))


def remove_wishlist(request, product_id: int):
    wishlist = Wishlist(request)
    wishlist.remove(product_id)

    return redirect(request.META.get('HTTP_REFERER'))


def clear_wishlist(request):
    wishlist = Wishlist(request)
    wishlist.clear()

    return redirect(request.META.get('HTTP_REFERER'))
