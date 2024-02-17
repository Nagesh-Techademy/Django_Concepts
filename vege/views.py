from django.shortcuts import render , redirect
from .models import *

# Create your views here.
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

def delete_receipe(request, id):
    print("delete", id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/vege/')


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