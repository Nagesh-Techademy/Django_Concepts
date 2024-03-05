from django.contrib import admin

# Register your models here.
from django.contrib import admin

from viewset.models import (Students)

# Register your models here.
admin.site.register(Students)

# @admin.register(Students)
# class StudentAdmin(admin.ModelAdmin):
#     list_display=['id','name','roll','city']