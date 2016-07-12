from django.shortcuts import render
from hospital.models import news,Doctor,register_note,Patient
from hospital.models import SignupForm,timeform
from accounts.models import MyProfile
from django.http import Http404
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect,HttpResponse
import json
from django.contrib.auth.decorators import login_required
from hospital.forms import wenzhen_form

def index(request):
    news_list=news.objects.all()
    news_list=news_list[::-1]
    print(request.user.get_group_permissions())
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
					return HttpResponseRedirect('/patient_home/')
				return HttpResponseRedirect('/home/')
			else:
				error.append('密码或用户名错误')
	else:
		signform = SignupForm() #获得表单对象
	return render(request,'doctor/login_doctor.html', {
        'form': signform,'error':error
        })

@login_required(login_url='/signup/')
def doctor_home(request):
	user = request.user.first_name
	register_note_list=register_note.objects.filter(doctor=Doctor.objects.get(user=request.user),finish=False)
	return render(request,'doctor/index.html',{'register_note_list':register_note_list,'user':user})




def ajax_used_to_select_doctor(request):
	department = request.GET['department']
	doctor_list=Doctor.objects.filter(department=department)
	doctor_name_list = []
	for obe in doctor_list:
		doctor_name_list.append(obe.name)
	return HttpResponse(json.dumps(doctor_name_list)) 


@login_required(login_url='/signup/')
def patient_home(request):
	if request.method == 'POST':
		department=request.POST['department']
		doctor_name=request.POST['doctor_name']
		optionsRadios=request.POST['optionsRadios']
		yueyu_time=request.POST['time'].replace("/",'-')
		if optionsRadios=='option1':
			after_afternoon=False
		else:
			after_afternoon=True
		paidui_number=register_note.objects.filter(doctor=Doctor.objects.get(name=doctor_name),time=yueyu_time,after_afternoon=after_afternoon).count()+1;
		register_note.objects.create(patient=MyProfile.objects.get(user=request.user),doctor=Doctor.objects.get(name=doctor_name),time=yueyu_time,after_afternoon=after_afternoon,paidui_number=paidui_number)
		return render(request,'patient/resignsuccess.html',{'patient_name':MyProfile.objects.get(user=request.user).name,'department':department,'doctor_name':doctor_name,'yueyu_time':yueyu_time,'paidui_number':paidui_number})
	else:
		return render(request,'patient/home.html',{'form':timeform})



def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

@login_required(login_url='/signup/')
def huizhen(request,id):
	if request.method == 'POST': # 如果表单被提交
		huizhen=request.POST['foo']
		detail_id = id
		register_detail=register_note.objects.get(id=id)
		register_detail.huizhen=huizhen
		register_detail.finish=True
		register_detail.save()
		return HttpResponseRedirect('/home/')
	else:
		detail_id = id
		register_detail=register_note.objects.get(id=id)
		register_detail_name=register_detail.patient.name
		return render(request,'doctor/detail.html',{'detail_id':detail_id,'wenzhen_form':wenzhen_form})


@login_required(login_url='/signup/')
def huizhen_history(request):
	user = request.user.first_name
	register_note_list=register_note.objects.filter(doctor=Doctor.objects.get(user=request.user),finish=True)
	return render(request,'doctor/huizhen_history.html',{'register_note_list':register_note_list,'user':user})

@login_required(login_url='/signup/')
def huizhen_history_detail(request,id):
	detail_id = id
	register_detail=register_note.objects.get(id=id)
	register_detail_name=register_detail.patient.name
	return render(request,'doctor/huizhen_history_detail.html',{'register_detail':register_detail,'wenzhen_form':wenzhen_form})


@login_required(login_url='/signup/')
def huizhen_history_patient(request):
	register_note_list=register_note.objects.filter(patient=MyProfile.objects.get(user=request.user))
	return render(request,'patient/huizhen_history.html',{'register_note_list':register_note_list})

@login_required(login_url='/signup/')
def huizhen_history_detail_patient(request,id):
	detail_id = id
	register_detail=register_note.objects.get(id=id)
	register_detail_name=register_detail.patient.name
	return render(request,'patient/huizhen_history_detail_patient.html',{'register_detail':register_detail,'wenzhen_form':wenzhen_form})


