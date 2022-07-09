"""swoosh_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from swoosh_app import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.productlist),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('productlist/', views.productlist, name='productlist'),
    path('productdetail/<int:id>', views.productdetail, name='productdetail'),
    path('cart/', views.cart, name='mycart'),
    path('myaccount/', views.profile, name='myaccount'),
    path('changepassword/', views.ChangePasswordView.as_view(), name='changepassword'),
    path('create-checkout-session', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/<str:session_id>/', views.success_payment, name='success'),
    path('orders/', views.myorders, name='orders'),
    path('order/<int:id>', views.order, name='order'),
    path('editproduct/<int:id>', views.editproduct, name='editproduct'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('editproductdetail/', views.editproductdetail, name='editproductdetail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
