from django.db import models
from django.contrib.auth.models import User


# for Soft delete(is_deleted field) # written in th manager
# class ReceipeManager(models.Manager):
#     def get_queryset(self) :
#         return  super().get_queryset().filter(is_deleted=False)


# Create your models here.
class Receipe(models.Model):
    user =models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    receipe_name =models.CharField(max_length=100)
    receipe_description= models.TextField()
    receipe_image= models.ImageField(upload_to="receipe")
    receipe_view_count=models.ImageField(default=1)
    is_deleted = models.BooleanField(default=False)

    #for Soft Delete
    # objects=ReceipeManager()# it will remove deleted recors and show
    admin_objects=models.Manager() # it will provide all details


class Department(models.Model):
    department=models.CharField(max_length=100)
#the __str__() method is defined to return the value of the department attribute of the model instance as a string.
    # So, when you call str() on an instance of the model, it will return the value of the department attribute.
    def __str__(self) -> str:
        return self.department

    #ordering in db meta is used
    class Meta:
        ordering=['department'] #sequence wise storing in db
    #If you have an instance of the Department model with department attribute set to "HR", calling str(instance) will return "HR"

#mediater which will connect student_id to Department
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self)-> str:
        return  self.student_id

#Foreignkey will be applyed on one to many field(Many relation one table)
class Student(models.Model):
    #each student will have only one department

    department=models.ForeignKey(Department, related_name='depart', on_delete=models.CASCADE) #models.CASCADE, it means that when a Department instance is deleted, all associated Student instances will also be deleted automatically.
    student_id=models.OneToOneField(StudentID, related_name='studentid', on_delete=models.SET_NULL, null=True, blank=True)
    student_name=models.CharField(max_length=100)
    student_email=models.EmailField(unique=True)
    student_age=models.IntegerField(default=18)
    student_address=models.TextField()

    def __str__(self)->str:
        return self.student_name

    class Meta:
        ordering =['student_name']
        verbose_name="student"# alias the student_name
      #  unique_together=['Student','Subject']
