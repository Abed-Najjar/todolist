import django.forms
from django.forms import ModelForm
from .models import List, Task, User
from django import forms


class LoginForm(forms.Form):
    UEmail = forms.EmailField(required=True, max_length=150, label="Your Email")
    UPassword = forms.CharField(
        required=True,
        max_length=150,
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class ListForm(ModelForm):
    class Meta:
        model = List
        fields = '__all__'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['UName','UEmail','UPassword']
