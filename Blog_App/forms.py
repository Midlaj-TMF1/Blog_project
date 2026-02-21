from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Blog_App.models import Login, Users, BlogPost


class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = Login
        fields = ['username','password1','password2']

class UsersRegister(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['name','email','bio','document']

class BlogPostRegister(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['Blog_detail','title','content','date','document']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }