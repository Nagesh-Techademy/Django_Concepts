from django.contrib import admin
from .models import Receipe
#or
from .models import *
# Register your models here.
admin.site.register(Receipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)

# Register your models here.
