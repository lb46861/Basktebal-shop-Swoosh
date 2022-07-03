from django.forms import ChoiceField, ModelForm
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone', 'password1', 'password2']

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone']
