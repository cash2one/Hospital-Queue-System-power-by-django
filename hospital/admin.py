from django.contrib import admin
from hospital.models import news,Doctor,Patient,register_note
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'workid','phonenumber','department',)
    list_filter = ('name',)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'author','content','time',)
    list_filter = ('tittle',)
class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'gender','identifyid','phonenumber',)
	list_filter = ('name',)
class register_noteAdmin(admin.ModelAdmin):
	list_display = ('patient','doctor','finish', 'time',)
	list_filter = ('time',)



admin.site.register(register_note,register_noteAdmin)
admin.site.register(news,NewsAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
