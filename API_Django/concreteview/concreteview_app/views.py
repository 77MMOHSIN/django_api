from django.shortcuts import render
from .models import Student1
from .seiliazer import studentseializer
from rest_framework.generics import ListAPIView ,CreateAPIView,DestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
# Create your views here.

class Studentlist(ListAPIView,CreateAPIView):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
class Student_R_D(RetrieveUpdateAPIView,DestroyAPIView):
    queryset=Student1.objects.all()
    serializer_class=studentseializer