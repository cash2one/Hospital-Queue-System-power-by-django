from django.db import models
from django.contrib import admin

# Create your models here.
class news(models.Model):
    tittle = models.CharField(max_length=200)
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=5000)
    time=models.DateField(auto_now_add=True)


