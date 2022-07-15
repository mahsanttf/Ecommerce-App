from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    mobile = forms.IntegerField(min_value=0)
    address = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'mobile', 'address', 'email', 'username', 'password1', 'password2'
        )
