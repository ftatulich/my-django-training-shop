from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from shop.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class LoginForm(forms.Form):
    """Форма для входу на сайт"""
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "input",
                                                           "type": "email",
                                                           'name': "email",
                                                           'placeholder': "Email"
                                                           }))
    password = forms.CharField(max_length=128, widget=forms.PasswordInput(attrs={'class': "input",
                                                                                 'type': "password",
                                                                                 'name': "address",
                                                                                 'placeholder': "Password"
                                                                                 }))


class RegisterForm(forms.ModelForm):
    """Форма для реєстрації"""

    class Meta(object):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': "input",
                                               "type": "text",
                                               'name': "first-name",
                                               'placeholder': "Ім'я користувача"
                                               }),
            'first_name': forms.TextInput(attrs={'class': "input",
                                                 "type": "text",
                                                 'name': "first-name",
                                                 'placeholder': "Ім'я"
                                                 }),
            'last_name': forms.TextInput(attrs={'class': "input",
                                                "type": "text",
                                                'name': "last-name",
                                                'placeholder': "Прізвище"
                                                }),
            'email': forms.TextInput(attrs={'class': "input",
                                            "type": "email",
                                            'name': "email",
                                            'placeholder': "Електронна пошта"
                                            }),
            'address': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "address",
                                              'placeholder': "Адреса"
                                              }),
            'city': forms.TextInput(attrs={'class': "input",
                                           'type': "text",
                                           'name': "city",
                                           'placeholder': "Місто"
                                           }),
            'country': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "county",
                                              'placeholder': "Країна"
                                              }),
            'zip_code': forms.TextInput(attrs={'class': "input",
                                               'type': "text",
                                               'name': "zip-code",
                                               'placeholder': "Поштовий Індекс"
                                               }),
            'password': forms.PasswordInput(attrs={'class': "input",
                                                   'type': "password",
                                                   'name': "address",
                                                   'placeholder': "Пароль"
                                                   })
        }


class EditProfileForm(forms.ModelForm):
    """Форма для реєстрації"""

    class Meta(object):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code')
        widgets = {
            'username': forms.TextInput(attrs={'class': "input",
                                               "type": "text",
                                               'name': "first-name",
                                               'placeholder': "Ім'я користувача"
                                               }),
            'first_name': forms.TextInput(attrs={'class': "input",
                                                 "type": "text",
                                                 'name': "first-name",
                                                 'placeholder': "Ім'я"
                                                 }),
            'last_name': forms.TextInput(attrs={'class': "input",
                                                "type": "text",
                                                'name': "last-name",
                                                'placeholder': "Прізвище"
                                                }),
            'email': forms.TextInput(attrs={'class': "input",
                                            "type": "email",
                                            'name': "email",
                                            'placeholder': "Електронна пошта"
                                            }),
            'address': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "address",
                                              'placeholder': "Адреса"
                                              }),
            'city': forms.TextInput(attrs={'class': "input",
                                           'type': "text",
                                           'name': "city",
                                           'placeholder': "Місто"
                                           }),
            'country': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "county",
                                              'placeholder': "Країна"
                                              }),
            'zip_code': forms.TextInput(attrs={'class': "input",
                                               'type': "text",
                                               'name': "zip-code",
                                               'placeholder': "Поштовий Індекс"
                                               }),
        }


class ChangePermissionsForm(forms.Form):
    PERMISSIONS = (
        ('change_permission', 'Змінювати права інших користувачів'),
        ('delete_customuser', 'Видаляти Користувачів'),
        ('change_products', 'Схвалювати Товари'),
        ('change_category', 'Додавати категорії'),
    )

    permissions = forms.MultipleChoiceField(choices=PERMISSIONS, widget=forms.CheckboxSelectMultiple(), required=False)
