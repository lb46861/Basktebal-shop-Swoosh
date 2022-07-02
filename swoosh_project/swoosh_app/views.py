from hashlib import blake2b
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import Product, ProductDetail, Order, OrderDetails
import uuid, random
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


def addToCart(request, myProduct):
    #number = uuid.uuid1(random.randint(0, 281474976710655))
    customer = request.user
    order, created = Order.objects.get_or_create(customer_id = customer, status='cart')
    itemDetail, created = OrderDetails.objects.get_or_create(order_id=order, product=myProduct)
    if myProduct.quantity > 0:
        itemDetail.quantity += 1
        itemDetail.save()
        myProduct.quantity -= 1
        myProduct.save()
        return 'Product addedd successfully!'
    else:
        return 'No more products left in stock!'


def removeOne(request, myProduct):
    customer = request.user
    order = Order.objects.get(customer_id = customer, status='cart')
    itemDetail = OrderDetails.objects.get(order_id=order, product=myProduct)
    if itemDetail.quantity == 1:
        itemDetail.delete()
    else:
        itemDetail.quantity -= 1
        itemDetail.save()
    myProduct.quantity += 1
    myProduct.save()
    return 'Product removed successfully!'



def removeAll(request, myProduct):
    customer = request.user
    order = Order.objects.get(customer_id = customer, status='cart')
    itemDetail = OrderDetails.objects.get(order_id=order, product=myProduct)
    while itemDetail.quantity > 0:
        itemDetail.quantity -= 1
        myProduct.quantity += 1
    itemDetail.delete()
    myProduct.save()
    return 'Products removed successfully!'



def productdetail(request, id):
    if request.method == 'POST':
        productDetailID = request.POST['myproduct']
        myProduct = ProductDetail.objects.get(id = productDetailID)
        option = request.POST['option']
        if option == 'tocart':
            addToCart(request, myProduct)
        elif option == 'buy':
            addToCart(request, myProduct)
            return redirect('mycart')

    product = Product.objects.get(id = id)
    productdetail = ProductDetail.objects.filter(product_id = id)
    #available = len(productdetail.values_list('product_id', flat=True))
    similiarProducts = Product.objects.filter(category_id = product.category_id).exclude(id=product.id)

    data = {
        'product': product,
        'productdetail' : productdetail,
        #'available': available,
        'similiarProducts': similiarProducts,
    }
    return render(request, 'products/productdetail.html',data)


def cart(request):
    stock = ''
    if request.method == 'POST':
        productDetailID = request.POST['myproduct']
        myProduct = ProductDetail.objects.get(id = productDetailID)
        option = request.POST['option']
        if option == 'add':
            stock = addToCart(request, myProduct)
        elif option == 'removeOne':
            stock = removeOne(request, myProduct)
        elif option == 'removeAll':
            stock = removeAll(request, myProduct)

    customer = request.user
    order, created = Order.objects.get_or_create(customer_id = customer, status='cart')
    cartItems = order.orderdetails_set.all()
    data = {
        'cartItems': cartItems,
        'order': order,
        'stock': stock
    }

    return render(request, 'account/mycart.html', data)