from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from Blog_App.forms import UsersRegister, LoginRegister, BlogPostRegister
from Blog_App.models import Users, BlogPost


# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def admin_home(request):
    return render(request, 'admin/admin.html')

def users_home(request):
    return render(request, 'users/users_home.html')



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect('admin_home')
            else:
                return redirect('users_home')

        else:
            messages.info(request, 'invalid credentials')

    return render(request, 'login.html')













