from django.shortcuts import render
from rest_framework.response import Response
from .models import Student1
from .seiliazer import studentseializer
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
class STudentviewset(viewsets.ViewSet):
    def list(self,request):
        stu=Student1.objects.all()
        serilizer=studentseializer(stu,many=True)
        return Response(serilizer.data)
    def retrieve(self, request,pk=None):
        id=pk
        if id is not None:
            
            stu=Student1.objects.get(id=id)
            serilizer=studentseializer(stu)
            return Response(serilizer.data)
    def create(self,request):
        serializer=studentseializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'post is created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk):
        id=pk
        stu=Student1.objects.get(pk=id)
        serializer=studentseializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'post is created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id=pk
        stu=Student1.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data Deleted'})    
            
    