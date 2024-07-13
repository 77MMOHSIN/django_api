from django.shortcuts import render
import io
from django.http import HttpResponse
from .seriliazer import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from .models import Student
from .seriliazer import StudentSerializer
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)        
            serilizer=StudentSerializer(stu)
            json_data1=JSONRenderer().render(serilizer.data)
            return HttpResponse(json_data1,content_type='application/json')
        stu=Student.objects.all()
        serilizer=StudentSerializer(stu, many=True)
        json_data1=JSONRenderer().render(serilizer.data)
        return HttpResponse(json_data1,content_type='application/json') 
   
    if request.method=='POST':
        json_data=request.body
        streampost=io.BytesIO(json_data)
        pythondatapost=JSONParser().parse(streampost)
        serilizerpost=StudentSerializer(data=pythondatapost)
        
        if serilizerpost.is_valid():
            serilizerpost.save()
            response={'message':'data Created'}
            json_datapost=JSONRenderer().render(response)
            return HttpResponse(json_datapost,content_type='application/json')
        json_datapost=JSONRenderer().render(serilizerpost.errors)
        return HttpResponse(json_datapost,content_type='application/json')            
    if request.method=='PUT':
        json_data=request.body
        databtyes=io.BytesIO(json_data)
        pythondataput=JSONParser().parse(databtyes)
        id=pythondataput.get('id')
        datamodel=Student.objects.get(id=id)
        # convert into api class ma
        apiclass=StudentSerializer(datamodel ,data=pythondataput,partial=True)
        if apiclass.is_valid():
            apiclass.save()
            response={'message':'Data updated !!!!!!'}
            show=JSONRenderer().render(response)
            return HttpResponse(show,content_type='application/json')
        show=JSONRenderer().render(apiclass.errors)
        return HttpResponse(show,content_type='application/json')
    if request.method=='DELETE':
        jsondata=request.body
        convertintobytes=io.BytesIO(jsondata)
        covertintopython=JSONParser().parse(convertintobytes)
        id=covertintopython.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        response={'messages':'delete successfully!!!!!!!!!'}
        jsondatarender=JSONRenderer().render(response)
        return HttpResponse(jsondatarender,content_type='applicaton/json')
        
        
        
        
                
            
        
        
        
        
        
    