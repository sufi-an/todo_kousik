from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# ENUMS


class User(AbstractUser): 
    fist_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    photo=models.ImageField(blank=True,null=True)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

    def __str__(self):
        return self.email



# class Task(models.Model):
#     title=models.CharField(max_length=150)
#     description=models.CharField(max_length=450)
#     due_date=models.DateField()

#     created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
#     updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
#     def __set__(self):
#         return self.title

 
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=450)
    due_date=models.DateField()

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    def __set__(self):
        return self.title
