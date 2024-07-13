from django.shortcuts import render
from .models import Student1
from .seiliazer import studentseializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin

# Create your views here.
class genericlist(GenericAPIView,ListModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
        
class studentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
class studentretriev(GenericAPIView,RetrieveModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

class studentupdate(GenericAPIView,UpdateModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
class studentdelete(GenericAPIView,DestroyModelMixin):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

