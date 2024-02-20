from django.contrib import admin
from .models import Receipe
#or
from .models import *
# Register your models here.
admin.site.register(Receipe)

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)

#
# #To shere the extra data from other tables
# Class ReportCardAdmin(admin.ModelAdmin):
#     list_display=['student','student_rank', 'total_marks','date_of_report_card_genration']
#     ordering=['-student_rank']
#     #we don't have a total_mark
#     def total_marks(self, obj): # in obj details will come from reportCard
#         subject_marks= SubjectMarks.objects.filter(student=obj.student)
#         marks=(subject_marks.aggregate(marks=Sum('marks')))
#         return (marks['marks'])
#
# admin.site.register(ReportCard, ReportCardAdmin)
# # Register your models here.
