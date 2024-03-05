from django.shortcuts import render
from .models import Students
from .serializers import StudentSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
# Create your views here.

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializers



