from django.shortcuts import render

from Blog_App.models import BlogPost, Users


def blog_list(request):
    data = BlogPost.objects.all()
    return render(request, 'admin/blog_list.html', {'data':data})


def users_list(request):
    data = Users.objects.all()
    return render(request,"admin/users_list.html",{"data":data})