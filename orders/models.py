from django.db import models
from shop.models import Product


class Order(models.Model):
    """Інформація про замолення"""
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    email = models.EmailField("email address", unique=True, db_index=True)
    address = models.TextField("user`s address")
    city = models.TextField('user`s city')
    country = models.TextField('user`s country')
    zip_code = models.TextField('user`s zip code')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    notes = models.TextField(max_length=320, blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.alL())


class OrderItem(models.Model):
    """Модель товару із замовлення"""
    order = models.ForeignKey("Order", related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_item', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.id}"

    def get_cost(self):
        return self.price * self.quantity


