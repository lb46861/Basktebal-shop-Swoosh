from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import Product
# Create your views here.
 

def register(request):   
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
         form = UserForm()
    
    return render(request, 'account/register.html', {'form':form})


def productlist(request):
    products = Product.objects.all()

    return render(request, 'products/productlist.html', {'products': products})