from django.db import models

# Create your models here.
class student(models.Model) :
    name= models.CharField(max_length=100)
    age= models.IntegerField()
    email= models.EmailField()
    address = models.TextField(blank=True,null=True)
    file = models.FileField()
    #id= models.AutoField() : it will automatically adds

class Product(models.Model):
    pass


class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed =models.IntegerField(default=50)
