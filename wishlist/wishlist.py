from shop.models import Product
from django.conf import settings


class Wishlist(object):
    """Клас для роботи з списком товарів за якими слідкує користувач"""

    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get(settings.WISHLIST_SESSION_ID)

        if not wishlist:
            wishlist = self.session[settings.WISHLIST_SESSION_ID] = []

        self.wishlist = wishlist

    def add(self, product_id: int) -> None:
        """Додаємо айдішник товарів в список"""
        if product_id not in self.wishlist:
            self.wishlist.append(product_id)

        self.save()

    def save(self) -> None:
        """Зберігає зміни в сессії"""
        self.session[settings.WISHLIST_SESSION_ID] = self.wishlist
        self.session.modified = True

    def remove(self, product_id: int) -> None:
        """видаляє товар зі списку товарів"""
        if product_id in self.wishlist:
            self.wishlist.remove(product_id)

        self.save()

    def __iter__(self):
        products = Product.objects.filter(id__in=self.wishlist)

        for product in products:
            yield product

    def clear(self):
        del self.session[settings.WISHLIST_SESSION_ID]
        self.session.modified = True

    def __len__(self):
        return len(self.wishlist)
