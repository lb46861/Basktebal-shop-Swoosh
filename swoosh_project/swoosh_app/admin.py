from django.contrib import admin
from .models import User, Role, Order, Team, Category, Brand, Product, OrderDetails, Size
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('None', {'fields':('role_id', 'address', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('None', {'fields':('role_id', 'address', 'phone')}),
    )
    
admin.site.register(Role)
admin.site.register(Order)
admin.site.register(Team)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Size)
admin.site.register(OrderDetails)