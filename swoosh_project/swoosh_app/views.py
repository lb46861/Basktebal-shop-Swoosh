from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
# Create your views here.
 

def register(request):
    if request.method == 'GET':
        form = UserForm()
        return render(request, 'register.html', {'form':form})

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('Something went wrong!')
