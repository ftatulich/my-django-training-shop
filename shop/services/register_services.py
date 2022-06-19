from django.shortcuts import render, redirect
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import ValidationError
from shop.forms.profile_forms import RegisterForm

htmlresponse = str


def validate_register(request) -> htmlresponse:
    """Логіка строрінки входу, якщо форма заповнена(post) перевіряє чи все ок,
        якщо ні рендерить сторінку регістрації"""
    context = {}

    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        return _register_form_post(request, context)

    form = RegisterForm()
    context['form'] = form

    return render(request, 'shop/register.html', context)


def _register_form_post(request, context: dict) -> htmlresponse:
    """Перевіряє валідність форми, правильність даних, якщо вони вірні зберігає юзера """
    form = RegisterForm(request.POST)
    if form.is_valid():
        try:
            validate_password(form.cleaned_data['password'])

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')
        except ValidationError:
            form.add_error('password', error='Пароль не повинен бути настільки легким')
            context['form'] = form

            return render(request, 'shop/register.html', context)
    else:
        return render(request, 'shop/register.html', context)
