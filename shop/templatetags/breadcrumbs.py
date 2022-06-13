from django import template

register = template.Library()


@register.simple_tag(name='breadcrumbs')
def breadcrumbstag(request):
    path = []
    for url_element in request.path.replace('/', ' ').strip().split():
        path.append(url_element)

    return path
