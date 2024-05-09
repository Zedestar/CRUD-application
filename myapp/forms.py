from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import record



# - Creating user. Through user Login form
# - Oncreating user we should import UserCreationForm and User for the user fields
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',  'email', 'password1', 'password2']


# - Now Crating user Login form.
# - Oncreating user login we need to import AuthenticationForm and  widget for PasswordInput and TextInput
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)
    

class CreateDataForm(forms.ModelForm):
    class Meta:
        model = record
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'city', 'country']
