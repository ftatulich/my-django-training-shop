from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


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
        fields = ('first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "input",
                                                 "type": "text",
                                                 'name': "first-name",
                                                 'placeholder': "First Name"
                                                 }),
            'last_name': forms.TextInput(attrs={'class': "input",
                                                "type": "text",
                                                'name': "last-name",
                                                'placeholder': "Last Name"
                                                }),
            'email': forms.TextInput(attrs={'class': "input",
                                            "type": "email",
                                            'name': "email",
                                            'placeholder': "Email"
                                            }),
            'address': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "address",
                                              'placeholder': "Address"
                                              }),
            'city': forms.TextInput(attrs={'class': "input",
                                           'type': "text",
                                           'name': "city",
                                           'placeholder': "City"
                                           }),
            'country': forms.TextInput(attrs={'class': "input",
                                              'type': "text",
                                              'name': "county",
                                              'placeholder': "Country"
                                              }),
            'zip_code': forms.TextInput(attrs={'class': "input",
                                               'type': "text",
                                               'name': "zip-code",
                                               'placeholder': "ZIP Code"
                                               }),
            'password': forms.PasswordInput(attrs={'class': "input",
                                                   'type': "password",
                                                   'name': "address",
                                                   'placeholder': "Password"
                                                   })
        }
