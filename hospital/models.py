from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget

# Create your models here.
class news(models.Model):
    tittle = models.CharField(u'标题',max_length=200)
    author = models.CharField(u'作者',max_length=20)
    content = models.CharField(u'内容',max_length=5000)
    time=models.DateField(u'日期',auto_now_add=True)
    def __unicode__(self):
    	return self.tittle
    class Meta:
    	verbose_name='新闻'
    	verbose_name_plural='新闻管理'

class Doctor(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(u'姓名',max_length=10)
	workid = models.CharField(u'工号',max_length=10)
	department = models.CharField(u'科室',max_length=11)
	phonenumber = models.CharField(u'手机号',max_length=11)
	def __str__(self):
		return '姓名'+self.name+'工号'+self.workid
	class Meta:
		verbose_name='医生'
		verbose_name_plural='医生管理'

class Patient(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(u'姓名',max_length=10)
	gender=models.BooleanField(u'性别',null=False,default=True)
	identifyid = models.CharField(u'身份证号',max_length=18)
	phonenumber = models.CharField(u'手机号',max_length=11)
	def __str__(self):
		return '姓名'+self.name+'身份证号'+self.identifyid
	class Meta:
		verbose_name='患者'
		verbose_name_plural='患者管理'

class register_note(models.Model):
	patient = models.ForeignKey(Patient)
	doctor = models.ForeignKey(Doctor)
	finish=models.BooleanField(u'完成挂诊',null=False,default=False)
	time=models.DateField(u'日期')
	paidui_number=models.IntegerField(u'队列号',null=False)
	create_time=models.DateTimeField(u'创建日期',auto_now_add=True)
	after_afternoon=models.BooleanField(u'上午还是下午',null=False,default=False)

	def __str__(self):
		return self.patient.name
	class Meta:
		verbose_name='挂诊'
		verbose_name_plural='挂诊管理'


# my form

class SignupForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),max_length=100 ,label='用户名',error_messages={'required':u'用户名不能为空'})
	password = forms.CharField(label='密码',widget=forms.PasswordInput(attrs={'class': 'form-control'}),error_messages={'required':u'密码不能为空'})




class timeform(forms.Form):
	time = forms.DateField(widget=DateWidget(usel10n=True, bootstrap_version=3))