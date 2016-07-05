from django import forms
from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm

from collections import OrderedDict


class SignupFormExtra(SignupForm):
    """
    A form to demonstrate how to add extra fields to the signup form, in this
    case adding the first and last name.


    """
    GENDER_CHOICES = (
        (1, _('男性')),
        (2, _('女性')),
        )

    name = forms.CharField(label=_(u'姓名'),
                                 max_length=30,
                                 required=False)
    gender = forms.ChoiceField(label=_('性别'),
        choices=GENDER_CHOICES)
    identifyid = forms.CharField(label=u'身份证号',max_length=18)
    birth_date = forms.DateField(label=u'出生日期');
    phonenumber = forms.CharField(label=u'手机号',max_length=11)

    def save(self):
        # First save the parent form and get the user.
        new_user = super(SignupFormExtra, self).save()
        new_user.name = self.cleaned_data['name']
        new_user.gender = self.cleaned_data['gender']
        new_user.birth_date = self.cleaned_data['birth_date']
        new_user.identifyid = self.cleaned_data['identifyid']
        new_user.phonenumber = self.cleaned_data['phonenumber']
        new_user.update(name=self.cleaned_data['name'])
        new_user.save()
        return new_user