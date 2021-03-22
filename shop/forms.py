from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order, Review


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=250, help_text='example@mail.ru')
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        labels = {
            'username': 'имя пользователя',
            'password1': 'пароль',
            'password2': 'повторите пароль',
        }
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': 'в формате\
             7*** *** ** **'}),
        }


form = SignUpForm()


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = {'name', 'text'}
        labels = {
            'name': '',
            'text': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'ВВЕДИТЕ ВАШЕ ИМЯ'}),
            'text': forms.Textarea(attrs={
                'placeholder': 'НАПИШИТЕ, ПОЖАЛУЙСТА, ОТЗЫВ.'})
        }


class OrderForm(ModelForm):
     class Meta:
         model = Order
         fields = '__all__'
         labels = {
             'last_name': 'Фамилия',
             'first_name': 'Имя',
             'father_name': 'Отчество',
             'phone': 'Телефон',
             'birth_date': 'Дата рождения',
             'living_address': 'Адрес проживания',
             'living_index': 'Индекс проживания',
             'registration_address': 'Адрес прописки',
             'registration_index': 'Индекс прописки',
             'passport_organization': 'Кем выдан паспорт?',
             'passport_date': 'Дата выдачи паспорта',
             'passport_series': 'Серия паспорта',
             'passport_number': 'Номер паспорта',
         }
         this_year = datetime.today().year
         date_range = 100
         widgets = {
             'birth_date': forms.SelectDateWidget(years=range(
                 this_year - date_range, this_year - 17)),
             'passport_date': forms.SelectDateWidget(years=range(
                 this_year - date_range, this_year)),
         }
