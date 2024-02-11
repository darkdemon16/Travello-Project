from django.contrib.auth.forms import UserCreationForm
from .models import PassengerDetail
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']

class PassengerDetailForm(forms.ModelForm):
    class Meta:
        model = PassengerDetail
        fields = ['pid','first_name','last_name', 'age', 'date_created', 'phone']