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


  def __init__(self, *args, **kwargs):
      super(UserForm, self).__init__(*args, **kwargs)
      # Making location required
      self.fields['first_name'].required = True
      self.fields['last_name'].required = True

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

class UpdateUserForm(ModelForm):
  
  def __init__(self, *args, **kwargs):
      super(UpdateUserForm, self).__init__(*args, **kwargs)
      self.fields['username'].required = True
      self.fields['first_name'].required = True
      self.fields['last_name'].required = True
      self.fields['email'].required = True

  class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',  'phone' ]


class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = '__all__'

class ProductDetailForm(ModelForm):
  class Meta:
    model = ProductDetail
    fields = '__all__'


class OrderForm(ModelForm):
  class Meta:
    model = Order
    fields = '__all__'

class AddressForm(ModelForm):
  class Meta:
    model = City
    fields =  ('country', 'name')

class PostalForm(ModelForm):
  class Meta:
    model = Postal
    fields =  ('postal_code',)


class AddressForm(ModelForm):
  class Meta:
    model = Address
    fields =  ('address',)