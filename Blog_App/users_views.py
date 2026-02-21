from django.contrib.auth import logout
from django.shortcuts import render, redirect

from Blog_App.forms import UsersRegister, BlogPostRegister, LoginRegister
from Blog_App.models import Users, BlogPost


def users_add(request):
    if request.method == "POST":
        usr_form = UsersRegister(request.POST, request.FILES)
        login_form = LoginRegister(request.POST)

        if usr_form.is_valid() and login_form.is_valid():
            login = login_form.save(commit=False)
            login.is_users = True
            login.save()

            users = usr_form.save(commit=False)
            users.users_detail = login
            users.save()

    else:
        usr_form = UsersRegister()
        login_form = LoginRegister()
    return render(request, 'Register.html', {'usr_form':usr_form, 'login_form':login_form})

def profile(request):
    data = request.user
    profile = Users.objects.get(users_detail=data.id)
    return render(request,"users/profile.html",{"data":profile})

def profile_edit(request):

    user=request.user
    bloger=Users.objects.get(users_detail=user)

    if request.method == "POST":
        blo_form = UsersRegister(request.POST, instance=bloger)
        if blo_form.is_valid():
            blo_form.save()
            return redirect('profile')
    else:
        blo_form = UsersRegister(instance=bloger)
    return render(request,"users/profile_edit.html",{"data":blo_form})

def blog_add(request):
    if request.method == "POST":
        blog_form = BlogPostRegister(request.POST, request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('admin_home')
    else:
        blog_form = BlogPostRegister()

    return render(request, "users/blog_add.html", {"blog_form": blog_form})


def blo_list(request):
    data = BlogPost.objects.all()
    return render(request, 'users/blog_lists.html', {'data': data})

def blog_edit(request,id):
    user=request.user
    blog=BlogPost.objects.get(id=id)
    if request.method == "POST":
        blog_form = BlogPostRegister(request.POST, instance=blog)
        if blog_form.is_valid():
            blog_form.save()
            return redirect('blo_list')
    else:
        blog_form = BlogPostRegister(instance=blog)
    return render(request,"users/blog_edit.html",{"data":blog_form})

def blog_delete(request, id):
    bus_delete = BlogPost.objects.get(id=id)
    bus_delete.delete()
    return redirect('blo_list')

def Logout_users(request):
    logout(request)
    return redirect('index')