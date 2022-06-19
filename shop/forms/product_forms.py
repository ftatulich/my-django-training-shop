from django import forms
from shop.models import Product


class AddProductForm(forms.ModelForm):
    class Meta(object):
        model = Product
        fields = ('name', 'price', 'amount', 'description', 'category', 'preview')
        widgets = {
            'name': forms.TextInput(attrs={'class': "input",
                                           "type": "text",
                                           'placeholder': "Назва товару"
                                           }),
            'price': forms.TextInput(attrs={'class': "input",
                                            "type": "text",
                                            'placeholder': "Ціна"
                                            }),
            'amount': forms.NumberInput(attrs={'class': "input"}),
            'preview': forms.FileInput(),
        }


class EditProductForm(forms.ModelForm):
    class Meta(object):
        model = Product
        fields = ('name', 'price', 'amount', 'description', 'category', 'preview')
        widgets = {
            'name': forms.TextInput(attrs={'class': "input",
                                           "type": "text",
                                           'placeholder': "Назва товару"
                                           }),
            'price': forms.TextInput(attrs={'class': "input",
                                            "type": "text",
                                            'placeholder': "Ціна"
                                            }),
            'amount': forms.NumberInput(attrs={'class': "input"}),
            'preview': forms.FileInput(),
        }
