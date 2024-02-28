
from django.contrib import admin

from django.urls import path, include

#from api.views import student_api     # Function Based View
from api.views import StudentAPI
from home.views import *
from vege.views import *

urlpatterns = [
    #path('studentapi/', student_api, name="student_api"),                              # Function Based view
    path('studentapi/', StudentAPI.as_view(), name="student_api_classBase"),            # Class Based view
]
