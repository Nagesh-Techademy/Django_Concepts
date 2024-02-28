import io

from django.shortcuts import render
from rest_framework.parsers import JSONParser
from api.serializers import StudentSerializer
from api.models import Students
from rest_framework.renderers import  JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None) # it will be like if ID is present then it will take ID other Wise None
        if id is not None:
            stu=Students.objects.get(id=id)
            serializer= StudentSerializer(stu)
            json_data= JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        stu= Students.objects.all()
        serializer = StudentSerializer(stu, many=True)
        json_data = JSONRenderer().render(serializer.data)
        # a=HttpResponse(json_data, content_type='application/json')  #For checking Purpose
        # print(a.json)
        # print('view')
        return HttpResponse(json_data, content_type='application/json')


    #POST
    if request.method == 'POST':
        json_data=request.body #JsonData
        stream=io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream) ##PythonData
        serializer=StudentSerializer(data = pythondata) ##complex data
        if serializer.is_valid():
            serializer.save()
            res ={'msg':'Data Created'}
            json_data=JSONRenderer().render(res)                       # need to check this one for bracket
            return HttpResponse(json_data, content_type='application/json')
        error_data = JSONRenderer.render(serializer.errors)                        #If error Comes
        return HttpResponse(error_data, content_type='application/json')

    #Update/Put
    if request.method == 'PUT':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Students.objects.get(id=id)
        #serializer = StudentSerializer(stu, data=pythondata, partial=True)   # Partial Update
        serializer = StudentSerializer(stu, data=pythondata)  # Partial Update
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        error_data = JSONRenderer.render(serializer.errors)  # If error Comes
        return HttpResponse(error_data, content_type='application/json')

    #Delete
    if request.method == 'DELETE':
        json_data=request.body
        stream= io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Students.objects.get(id=id)
        stu.delete()
        res={'msg': 'Data Deleted'}
        # json_data=JSONRenderer().render(res)
        # return  HttpResponse(json_data, content_type='application/json')

        # Instated of these two lines Use one line by importing   'JsonResponse'
        return JsonResponse(res, safe=False)








