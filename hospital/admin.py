from django.contrib import admin
from hospital.models import news,Doctor,register_note
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class DoctorAdmin(SummernoteModelAdmin):
    list_display = ('name', 'workid','phonenumber','department',)
    list_filter = ('name',)
class NewsAdmin(SummernoteModelAdmin):
    list_display = ('tittle','content','time',)
    list_filter = ('tittle',)
class register_noteAdmin(SummernoteModelAdmin):
	list_display = ('patient','doctor','finish', 'time',)
	list_filter = ('time',)



admin.site.register(register_note,register_noteAdmin)
admin.site.register(news,NewsAdmin)
admin.site.register(Doctor,DoctorAdmin)
