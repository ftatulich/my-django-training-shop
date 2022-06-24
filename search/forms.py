from django import forms
from shop.models import Category


class SearchForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={"class": "input-select",
                                                                 'placeholder': "Всі категорії"}),
                                      required=False,)

    query = forms.CharField(widget=forms.TextInput(attrs={'class': "input",
                                                          'type': "text",
                                                          'name': "query",
                                                          'placeholder': "Пошук..."}))


class AdvancedSearchForm(SearchForm):
    price_min = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'price-min',
        'type': 'number',
    }))

    price_max = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'price-max',
        'type': 'number',
    }))


