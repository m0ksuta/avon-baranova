from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=250, help_text='example@mail.ru')
    last_name = forms.CharField(label='Фамилия', max_length=100)
    first_name = forms.CharField(label='Имя', max_length=100)
    father_name = forms.CharField(label='Отчество (при наличии)', required=False, max_length=100)
    birth_date = forms.DateField(label='Дата рождения (в формате \'дд/мм/гггг\')')
    living_address = forms.CharField(label='Адрес места проживания', max_length=500)
    living_index = forms.IntegerField(label='Индекс места проживания')
    registration_address = forms.CharField(label='Адрес места прописки', max_length=500)
    registration_index = forms.IntegerField(label='Индекс места прописки')
    passport_organization = forms.CharField(label='Кем выдан', max_length=500)
    passport_date = forms.DateField(label='Дата выдачи')
    passport_series = forms.IntegerField(label='Серия паспорта', max_value=9999, min_value=0000)
    passport_number = forms.IntegerField(label='Номер паспорта', max_value=999999, min_value=000000)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'father_name', 'password1', 'password2', 'email')


form = SignUpForm()
