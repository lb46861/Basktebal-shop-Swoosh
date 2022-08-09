
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import decimal
from django_countries.fields import CountryField


class Role(models.Model):
    role = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.role   


class Country(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name='cities')
    def __str__(self):
        return self.name

class Postal(models.Model):
    postal_code = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.postal_code


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    postal_code = models.ForeignKey(Postal, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
            return self.address

    

class User(AbstractUser):
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, default=1)
    phone = PhoneNumberField(null=True, blank=True, unique=False)
    location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    
    

class Order(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    number = models.CharField(max_length=100, null=True, unique=True)
    date = models.DateTimeField(null=True, blank=True) 
    status = models.CharField(max_length=100, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)


    @property
    def get_total(self):
        cartItems = self.orderdetails_set.all()
        total = 0
        for item in cartItems:
            total = decimal.Decimal(total) + item.get_total
        return total

    @property
    def get_total_stripe(self):
        cartItems = self.orderdetails_set.all()
        total = 0
        for item in cartItems:
            total = decimal.Decimal(total) + item.get_total
        return int(total * 100)

    def __str__(self):
        return f"Customer: {self.customer_id}; orderID: {self.id}; Date: {self.date}"

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
    size = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.size

class Product(models.Model):
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    name =  models.CharField(max_length=50, null=True)
    material = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    color = models.CharField(max_length=12, null=True, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

class ProductDetail(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    size_id = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.product_id} - {self.size_id}"

 
class OrderDetails(models.Model):
    product = models.ForeignKey(ProductDetail, on_delete=models.CASCADE, null=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(null=True, blank=True) 
    quantity = models.IntegerField(default = 0, null=True)
    status = models.CharField(max_length=100, null=True, blank=True)


    @property
    def get_total(self):
        total = self.product.product_id.price * self.quantity
        return total

    def __str__(self):
        return f"{self.id} - {self.product} - {self.order_id.id} - {self.date} - {self.quantity}"
