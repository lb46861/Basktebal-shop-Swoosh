from hashlib import blake2b
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import Product, ProductDetail
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


def productdetail(request, id):
    product = Product.objects.get(id = id)
    productdetail = ProductDetail.objects.filter(product_id = id)
    available = len(productdetail.values_list('product_id', flat=True))
    relatedProducts = Product.objects.filter(category_id = product.category_id).exclude(id=product.id)
    
    data = {
        'product': product,
        'productdetail' : productdetail,
        'available': available,
        'relatedProducts': relatedProducts,
    }
    return render(request, 'products/productdetail.html',data)
