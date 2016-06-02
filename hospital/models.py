from django.db import models

# Create your models here.
class news(models.Model):
    tittle = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    content = models.CharField(max_length=500)
    time=models.DateField(auto_now_add=True)