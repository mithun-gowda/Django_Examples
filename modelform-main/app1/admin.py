from django.contrib import admin

from .models import TrainerModel
# Register your models here.

class TrainerAdmin(admin.ModelAdmin):
    list_display=['empid','name']
    search_fields=['name'] 



admin.site.register(TrainerModel,TrainerAdmin)