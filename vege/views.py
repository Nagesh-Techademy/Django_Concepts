from django.shortcuts import render , redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required #decorator
#login is to mentain one session
#authenticate is used to che password is matching or not in encrypted format

# for Abstract User
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST       # to get the data from Frontend to backend
        files = request.FILES   # to grab the file
        receipe_image = files.get('receipe_image')
        receipe_name= data.get('receipe_name')
        receipe_description= data.get('receipe_description')



        Receipe.objects.create(
            receipe_image= receipe_image,
            receipe_name=receipe_name,
            receipe_description=receipe_description
        )
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        return redirect('/vege/') # To redirect to the same page

    queryset = Receipe.objects.all() # To get all Values

    if request.GET.get('search'):  # For search operation
        print(request.GET.get('search'))
        queryset= queryset.filter(receipe_name__icontains =request.GET.get('search'))

    context = {'receipes': queryset}  #need to use that receipes in html to feath the data
    return render(request, "receipes.html", context)
@login_required(login_url="/login/")
def delete_receipe(request, id):
    print("delete", id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/vege/')

@login_required(login_url="/login/")
def update_receipe(request, id):
    queryset = Receipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST  # to get the data from Frontend to backend
        files = request.FILES  # to grab the file
        receipe_image = files.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()
        return redirect('/vege/')

    context = {'receipe': queryset} # for passing te records
    print("update Page")
    return render(request, "update.html", context)


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, 'User is not present')
            return redirect("/login/") # need to give entire path

        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'invalid Credentials')
            return redirect("/login/")
        else:
            login(request, user)         #login session
            return redirect("/vege/")

    return render(request,'login.html')

#Nagesh
#Naik@123
def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method =="POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user= User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'UserName already taken')
            redirect("/register/")

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password= password
        )
        user.set_password("password") # For encription
        user.save()
        messages.info(request, 'User Registered')
        return render(request, "login.html")

    return render(request, "register.html")