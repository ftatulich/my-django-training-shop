from django.db.models import Q
from django.shortcuts import render

from search.forms import AdvancedSearchForm
from shop.models import Product


def search(request):
    query = request.GET.get('query')
    products = Product.objects.select_related('category').filter(
        Q(name__icontains=query) | Q(description__icontains=query)).order_by('-date').prefetch_related('images')
    advanced_search = AdvancedSearchForm()
    return render(request, 'search/search.html', {'products': products, 'advanced_search': advanced_search})
