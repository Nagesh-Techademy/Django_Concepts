from django.contrib import admin

from api.models import Students

# Register your models here.
#admin.site.register(Students)

@admin.register(Students)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']