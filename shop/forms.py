from django.forms import ModelForm
from shop.models import User


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


form = UserForm()
