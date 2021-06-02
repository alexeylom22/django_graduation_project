from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserOurRegistraion(UserCreationForm):
    email = forms.EmailField(
            label="Введите email",
            required=False,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите email'})
        )
    username = forms.CharField(
        label="Введите логин*",
        required=True,
        max_length=150,
        help_text='Обязательное поле. Не более 150 символом. Только буквы, цифры и символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите логин'})
    )
    password1 = forms.CharField(
        label="Введите пароль*",
        required=True,
        help_text='Пароль не должен быть маленьким и простым',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Введите пароль'})

    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
            label="Введите email",
            required=True,
            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите email'})
        )
    username = forms.CharField(
        label="Введите логин",
        required=True,
        help_text='Обязательное поле. Не более 150 символом. Только буквы, цифры и символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Введите логин'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']