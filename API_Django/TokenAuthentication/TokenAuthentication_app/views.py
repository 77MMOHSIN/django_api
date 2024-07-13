from django.shortcuts import render

# Create your views here.
from .models import Student1
from .seiliazer import studentseializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# this is basicAuthentication 

class studentmodelview(viewsets.ModelViewSet):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    # permission_classes=[IsAuthenticated]
    # permission_classes=[IsAdminUser]

    
    
    
    