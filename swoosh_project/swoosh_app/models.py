from ctypes import sizeof
from ipaddress import summarize_address_range
from math import degrees
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField




class Role(models.Model):
    role = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.role     

class User(AbstractUser):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, default=1)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = PhoneNumberField(null=True, blank=True, unique=True)


class Order(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=100, null=True, unique=True)
    date = models.DateTimeField(null=True, blank=True) 

    def __str__(self):
        return f"Customer: {self.customer_id}; orderID: {self.number}; Date: {self.date}"

class Team(models.Model):
    name =  models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name 

class Category(models.Model):
    name =  models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name 

class Brand(models.Model):
    name =  models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.name 

class Size(models.Model):
    size = models.CharField(max_length=5, null=True)
    def __str__(self):
        return self.size

class Product(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    name =  models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    color = models.CharField(max_length=12, null=True, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name

 
class OrderDetails(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    
    @property
    def get_total(self):
        total = self.product_id.price * self.quantity
        total_discount = total - self.discount * (total/100)
        return total_discount

    def __str__(self):
        return f"{self.product_id} - {self.order_id} - {self.total_price}"
