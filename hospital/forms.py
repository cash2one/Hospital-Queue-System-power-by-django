from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class wenzhen_form(forms.Form):
	foo = forms.CharField(widget=SummernoteWidget()) 