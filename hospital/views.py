from django.shortcuts import render
from hospital.models import news
from django.http import Http404

def index(request):
    news_list=news.objects.all()
    return render(request,'home/index.html',{'news_list':news_list})


def read_post(request,id):
	try:
		post_detail=news.objects.get(id=str(id))
	except news.DoesNotExist:
		raise Http404
	return render(request,'home/post.html',{'post_detail':post_detail})


def about(request):
	return render(request,'home/about.html')