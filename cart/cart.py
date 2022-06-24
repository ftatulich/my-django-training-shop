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

    def add(self, product_id: int, product_price: int, quantity: int = 1) -> None:
        """Додаємо товар у кошик, або обновляємо його кількість"""
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product_price)
            }

        self.save()

    def save(self):
        """Оновлення сесії"""
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product_id: int):
        """Видалення товару з кошику"""
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]

            self.save()

    def __iter__(self):
        """Ітератор який повертає товар з кошику його ціну та кількість"""
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)].update({
                'id': product.id,
                'photo': product.preview.url,
                'name': product.name,
                'total_price': self.cart[str(product.id)]['price'] * self.cart[str(product.id)]['quantity']
            })

            yield self.cart[str(product.id)]

    def __len__(self):
        """Кількість товарів в кошику"""
        return len(self.cart.keys())

    def clear(self):
        """Очищує кошик"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        """Подсчет стоимости товаров в корзине."""
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
