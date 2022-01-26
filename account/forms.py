from .models import User
from django import forms


class UserRegisterForm(forms.Form):
    email = forms.EmailField(max_length=125, label="ایمیل")
    password = forms.CharField(widget=forms.PasswordInput, label="رمز عبور")


class SuperUserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("email", "username", "password")
        labels = {
            "email": "ایمیل",
            "username": "نام کابری",
            "password": "رمز عبور",
        }
