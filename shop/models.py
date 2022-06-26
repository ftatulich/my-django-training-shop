
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser, PermissionsMixin):
    """Кастомна модель користувача"""
    username = models.CharField("username", unique=True, max_length=32)
    first_name = models.CharField("first name", max_length=150)
    last_name = models.CharField("last name", max_length=150)
    email = models.EmailField("email address", unique=True, db_index=True)
    address = models.TextField("user`s address")
    city = models.TextField('user`s city')
    country = models.TextField('user`s country')
    zip_code = models.TextField('user`s zip code')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return f'users/{self.pk}'


class Product(models.Model):
    """Модель товару на сайті"""
    name = models.CharField("product name", max_length=48)
    price = models.FloatField('product price', blank=False)
    old_price = models.FloatField('price before set discount', default=None, blank=True, null=True)
    amount = models.IntegerField('number of copies of the product', default=0)
    description = models.TextField('product description', default='Немає опису :( ')
    date = models.DateField('Product publicattion date', auto_now=True)
    category = models.ForeignKey('Category', related_name='product', on_delete=models.PROTECT, db_index=True)
    preview = models.ImageField(verbose_name='products preview', upload_to='photos/products/%Y/%m/%d')
    approved = models.BooleanField(default=False)
    seller = models.ForeignKey('CustomUser', verbose_name='Автор оголошення', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', args=(self.pk,))


class Category(models.Model):
    """Модель категорії продукту"""
    name = models.CharField("Category name", blank=False, db_index=True, unique=True, max_length=25)
    image = models.ImageField(verbose_name='category logo', upload_to='photos/category/%Y/%m/%d')

    def get_absolute_url(self):
        return f'categories/{self.name}'

    def __str__(self):
        return self.name


class Gallery(models.Model):
    """Модель для зберігння декількох фотогарфій для продукту"""
    image = models.ImageField(verbose_name='products image', upload_to='photos/products/%Y/%m/%d')
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)


class ProductReview(models.Model):
    product = models.ForeignKey('Product', on_delete=models.PROTECT, verbose_name='Ключ на товар')
    author = models.ForeignKey('CustomUser', on_delete=models.PROTECT, verbose_name='Автор відгуку')
    date = models.DateTimeField(verbose_name='Дата відгуку', auto_now=True)
    text = models.CharField(max_length=256, verbose_name='Текст Відгуку')
    rating = models.IntegerField(verbose_name='оцінка товару')

