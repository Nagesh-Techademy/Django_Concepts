from django.shortcuts import render

from django.http import HttpResponse
from .utils import send_email_to_client
# Create your views here.
def home(request):
    return render(request, 'index.html' )
def success_page(request):
    print("*" * 10)
    return HttpResponse("Login Successfully")

def dynamicdata(request):
    peoples =[
        {'name':'Nagesh Naik', 'age': 26},
        {'name': 'abc def', 'age': 10},
        {'name': 'hij klm', 'age': 35},
        {'name': 'nop qrst', 'age': 89}
    ]
    return render(request, 'dynamicdata.html', context={'peoples' : peoples} )

def email_send(request):
    send_email_to_client()
    return render(request, 'email.html')