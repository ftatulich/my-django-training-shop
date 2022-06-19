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

    def add(self, product_id: int, product_price: int, quantity: int = 1, update_quantity: bool = False) -> None:
        """Додаємо товар у кошик, або обновляємо його кількість"""
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product_price)
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
            self.cart[str(product.id)]['product'] = {
                'id': product.id,
                'photo': product.preview.url,
                'name': product.name,
            }

        for key in list(self.cart):
            self.cart[key]['price'] = float(self.cart[key]['price'])
            self.cart[key]['total_price'] = self.cart[key]['price'] * self.cart[key]['quantity']

            if not self.cart[key].get('product'):
                del self.cart[key]
                continue

            yield self.cart[key]

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
