from django.shortcuts import render
from .models import Student1
from .seiliazer import studentseializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin


#list  and create not required pk 
class glistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
#REtrieve update and destroy= pk required
class student_u_d(GenericAPIView,UpdateModelMixin,DestroyModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

 
    

