from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Product, Gallery, Category


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', )


admin.site.register(CustomUser, CustomUserAdmin)


class ImagesInline(admin.StackedInline):
    model = Gallery
    extra = 1
    max_num = 5


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'price', 'amount', 'preview')
    inlines = [ImagesInline]


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', )


admin.site.register(Category, CategoryAdmin)
