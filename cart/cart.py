from decimal import Decimal
from django.conf import settings
from shop.models import Product


class Cart(object):
    """Клас для роботи з кошиком"""

    def __init__(self, request):
        """Ініціалізуємо кошик"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart
        self.price = 0

    def add(self, product: Product, quantity: int = 1, update_quantity: bool = False):
        """Додаємо товар у кошик, або обновляємо його кількість"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """Оновлення сесії"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product: Product):
        """Видалення товару з кошику"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]

            self.save()

    def __iter__(self):
        """Перебір об'єктів Product і додавання їх в кошик"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            self.price += item['total_price']

            yield item

    def __len__(self):
        """Кількість товарів в кошику"""
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        """Очищує кошик"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
