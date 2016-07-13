from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile

class MyProfile(UserenaBaseProfile):
	GENDER_CHOICES = (
		(1, _('男性')),
		(2, _('女性')),
		)
	user = models.OneToOneField(User,
    	unique=True,
    	verbose_name=_('患者'),
    	related_name='患者管理')
	name = models.CharField(u'姓名',max_length=10)
	gender = models.PositiveSmallIntegerField(_('性别'),
		choices=GENDER_CHOICES,
		blank=True,
		null=True)
	age = models.IntegerField(u'年龄',null=True)
	identifyid = models.CharField(u'身份证号',max_length=18,null=True)
	phonenumber = models.CharField(u'手机号',max_length=11,null=True)
	about_me = models.TextField(_('关于我'), blank=True)
	class Meta:
		verbose_name='患者'
		verbose_name_plural='患者管理'
	def __str__(self):
		return self.name
