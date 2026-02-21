from django.contrib.auth import logout
from django.shortcuts import render, redirect

from Blog_App.models import BlogPost, Users


def blog_list(request):
    data = BlogPost.objects.all()
    return render(request, 'admin/blog_list.html', {'data':data})


def users_list(request):
    data = Users.objects.all()
    return render(request,"admin/users_list.html",{"data":data})

def users_delete(request, id):
    us_delete = Users.objects.get(id=id)
    us_delete.delete()
    return redirect('users_list')

def Logout_admin(request):
    logout(request)
    return redirect('index')