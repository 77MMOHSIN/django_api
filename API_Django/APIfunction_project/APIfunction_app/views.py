from django.shortcuts import render
from django.http import HttpResponse
# Create your views he
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .seiliazer import studentseializer



# Create your models here.
@api_view(['GET','POST','PUT','DELETE'])
def student_api(request):
# def student_api(request,pk=None):
    # id=pk
    
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None: 
            #convert into model
            stu=Student.objects.get(id=id)
            # api class
            apiclass=studentseializer(stu)
            return Response(apiclass.data)
        stu=Student.objects.all()
        apiclass=studentseializer(stu,many=True)
        return Response(apiclass.data)
            
    if request.method=='POST':
        serializer=studentseializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created post'})
        return Response(serializer.errors)

    if request.method=='PUT':
      id=  request.data.get('id')
      stu=Student.objects.get(pk=id)
      serializer=studentseializer(stu,data=request.data,partial=True)
      if serializer.is_valid():
            serializer.save()
            return Response({'message':'data is updates'})
      return Response(serializer.errors)
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'message':'data is deleted '})
        
        
          
    
      
      
      
        
        
            
        
                
        
    
    




# by defualt GET function 
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg':'hello world '})

# # POST METHOD
# @api_view(['PUT','GET','POST'])
# def hello_world(request):
#     if request.method=='PUT':
#         return Response({'msg':'this is PUT response'})
#     if request.method == 'GET':
#         return Response({'msg':'this is GET response'})
#     if request.method=='POST':
#         print(request.data)
#         return Response({'msg':'hello world POST REQUEST ','data':request.data})


