from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.simple_tag(name='breadcrumbs')
def breadcrumbstag(request):
    path = []
    for url_element in request.path.replace('/', ' ').strip().split():
        try:
            reverse(url_element)
            path.append(url_element)
        except NoReverseMatch:
            continue

    return path
