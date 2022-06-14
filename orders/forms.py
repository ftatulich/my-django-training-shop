from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'city', 'country', 'zip_code', 'notes')
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
            'notes': forms.Textarea(attrs={'class': 'input',
                                           'placeholder': 'Order notes',
                                           })
        }
