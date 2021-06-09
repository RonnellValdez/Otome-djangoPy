from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms  

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs= {'class': 'input is-success'}))    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'input is-success'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs= {'class': 'input is-success'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')

class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs= {'class': 'input is-success'}))    
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs= {'class': 'input is-success'}))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name')