
from django.contrib import admin
from django.urls import path, include
from vege.views import *

urlpatterns = [
    path('', receipes, name='receipes'),
    path('delete/<id>/', delete_receipe, name='delete_receipe'), #dynamic URL
    path('update/<id>/', update_receipe, name='update_receipe')
]
