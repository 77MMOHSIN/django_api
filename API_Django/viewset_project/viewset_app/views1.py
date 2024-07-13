from .models import Student1
from .seiliazer import studentseializer
from rest_framework import viewsets

class studentmodelview(viewsets.ModelViewSet):
    queryset=Student1.objects.all()
    serializer_class=studentseializer

class studentreadyonly(viewsets.ReadOnlyModelViewSet):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    