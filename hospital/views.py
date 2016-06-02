from django.shortcuts import render
from hospital.models import news

def index(request):
    return render(request,'home/index.html')