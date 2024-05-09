from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateDataForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout
from .models import record


# Create your views here.

def home(request):
    return render(request, 'myapp/home.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my_login")
    else:
        form = CreateUserForm()
    context = {
        'form':form
    }
    return render(request, 'myapp/register.html', context=context)

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username= username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('my_dashboard')
    else:
        form = LoginForm()
    context = {
        'form':form
    }
    return render(request, 'myapp/my_login.html', context=context)


def dashboard(request):
        data = record.objects.all()
        context = {
            'data':data,
        }
        return render(request, 'myapp/dashboard.html', context=context)

def create_record(request):
    if request.method == 'POST':
        form = CreateDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_dashboard')
    else:
        form = CreateDataForm()
    context = {
        'form':form
    }
    return render(request, 'myapp/create_record.html', context=context)

def view_item(request, pk):
    item = record.objects.get(id=pk)
    context = {
        'item':item
    }
    return render(request, 'myapp/view_item.html', context=context)

# - updating the selected item
def update_item(request, pk):
    update = record.objects.get(id=pk)
    if request.method == 'POST':
        data = CreateDataForm(request.POST, instance=update)
        if data.is_valid():
            data.save()
            return redirect("my_dashboard")
    else:
        data = CreateDataForm(instance=update)
    context = {
        'data':data,
        'update':update,
    }
    return render(request, 'myapp/update_item.html', context=context)



def delete_item(request, pk):
    item = record.objects.get(id=pk)
    item.delete()
    return redirect("my_dashboard")

def sign_out(request):
    auth.logout(request)
    return redirect("home")





