from django.contrib import admin
from hospital.models import news,Doctor
# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'workid','phonenumber','department',)
    list_filter = ('name',)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('tittle', 'author','content','time',)
    list_filter = ('tittle',)

admin.site.register(news,NewsAdmin)
admin.site.register(Doctor,DoctorAdmin)