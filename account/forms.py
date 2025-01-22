
from .models import Profile

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# UserCreationForm ->
# AuthenticationForm ->

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин ...'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль ...'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин ...'
    }))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль ...'
    }))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Повторите пароль ...'
    }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'age']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',

            })
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'age':'Возраст'

        }