from django.db.models import Q
from django.shortcuts import render

from search.forms import AdvancedSearchForm
from shop.models import Product


def search(request):
    products = Product.objects.filter(approved=True, name__icontains=request.GET.get('query'))

    return render(request, 'search/search.html', {'products': products})
