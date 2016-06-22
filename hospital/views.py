from django.shortcuts import render
from hospital.models import news,Doctor,register_note
from hospital.models import SignupForm
from django.http import Http404
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect

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



def signup(request):
	error =[]
	if request.method == 'POST': # 如果表单被提交
		signform = SignupForm(request.POST) # 获取Post表单数据
		if signform.is_valid(): # 验证表单
			username=signform.cleaned_data['username']
			password=signform.cleaned_data['password']

			user = authenticate(username=username, password=password)
			if (user is not None) and (user.is_active):
				login(request, user)
				try:
					Doctor.objects.get(user=request.user)
				except:
					return HttpResponseRedirect('/prhome/')
				return HttpResponseRedirect('/home/')
			else:
				error.append('密码或用户名错误')
	else:
		signform = SignupForm() #获得表单对象
	return render(request,'doctor/login_doctor.html', {
        'form': signform,'error':error
        })


def doctor_home(request):
	user = request.user.first_name
	register_note_list=register_note.objects.filter(doctor=Doctor.objects.get(user=request.user))
	return render(request,'doctor/index.html',{'register_note_list':register_note_list,'user':user})


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/signup/")