from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from shop.forms.profile_forms import LoginForm
from shop.models import CustomUser


def login_user_validate(request):
    """Рендерить форму входу, якщо користувач вже авторизований
        редіректить на головну сторінку"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == 'POST':
        return _form_check(request)

    login_form = LoginForm()
    return render(request, 'shop/login.html', {'form': login_form})


def _form_check(request):
    """Перевіряє валідність форми, якщо валідна, то логінить юзера,
        якщо ні - то повідомляє про це"""
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        email = login_form.cleaned_data['email']
        password = login_form.cleaned_data['password']

        return _login_user(request, email, password, login_form)

    login_form.add_error(field=None, error='Не правильний логін чи пароль')
    return render(request, 'shop/login.html', {'form': login_form})


def _login_user(request, email: str, password: str, login_form: LoginForm):
    """Перевіряє чи є користувач з таками данними, якщо тру логінить його"""
    try:
        user = CustomUser.objects.get(email=email)

        if user.check_password(password):
            login(request, user)
            return redirect('home')
        else:
            login_form.add_error(field=None, error='Не правильний логін чи пароль')
            return render(request, 'shop/login.html', {'form': login_form})

    except CustomUser.DoesNotExist:
        login_form.add_error(field=None, error='Не правильний логін чи пароль')
        return render(request, 'shop/login.html', {'form': login_form})
