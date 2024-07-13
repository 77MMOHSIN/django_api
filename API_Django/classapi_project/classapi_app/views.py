from django.shortcuts import render
from django.http import HttpResponse
# Create your views he
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student1
from .seiliazer import studentseializer
from rest_framework import status
from rest_framework.views import APIView
class student_Api(APIView):
    def get(self,request, format=None,pk=None):
        id=pk
        if id is not None:
            #convert into model
            stu=Student1.objects.get(id=id)
            # api class
            apiclass=studentseializer(stu)
            return Response(apiclass.data)
        stu=Student1.objects.all()
        apiclass=studentseializer(stu,many=True)
        return Response(apiclass.data)
    def post(self, request, format=None):
        serializer=studentseializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data is created post'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self, request,pk, format=None):
        id=pk
        stu=Student1.objects.get(pk=id)
        serializer=studentseializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'data is updates'})
        return Response(serializer.errors ,status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request,pk ,format=None):
        id=pk
        stu=Student1.objects.get(pk=id)
        serializer=studentseializer(stu,data=request.data ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":'partial data is updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request,pk, format=None):
        id=pk
        stu=Student1.objects.get(pk=id)
        stu.delete()
        return Response({'message':'data is deleted '},status=status.HTTP_400_BAD_REQUEST)
        
        
        
    

        

        

