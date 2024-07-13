from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from .seriallizer import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
#   model object single stuent data
def studnet_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')

# Query Set all student data
def studnet_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')