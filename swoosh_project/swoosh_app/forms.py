from dataclasses import field
from operator import mod
from django import forms
from django.forms import ChoiceField, ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
  email = forms.EmailField(required=True)

  def clean_email(self):
      if User.objects.filter(email=self.cleaned_data['email']).exists():
          raise forms.ValidationError("User with this email already exists.")
      return self.cleaned_data['email']

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone', 'city', 'country', 'postal_code', 'password1', 'password2']

class UpdateUserForm(ModelForm):
  class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'address', 'phone', 'city', 'country', 'postal_code']


class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = '__all__'

class ProductDetailForm(ModelForm):
  class Meta:
    model = ProductDetail
    fields = '__all__'

