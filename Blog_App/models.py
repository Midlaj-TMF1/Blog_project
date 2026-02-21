from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_Users = models.BooleanField(default=False)

class Users(models.Model):
    users_detail = models.OneToOneField('Login', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    bio = models.TextField()
    document = models.FileField(upload_to='documents/')
    def __str__(self):
        return self.name


class BlogPost(models.Model):
    Blog_detail = models.ForeignKey("Users", on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField()
    document = models.FileField(upload_to='documents/')


