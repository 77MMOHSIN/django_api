from .models import Student1
from .seiliazer import studentseializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny ,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import mypermission

# this is basicAuthentication 

# class studentmodelview(viewsets.ModelViewSet):
#     queryset=Student1.objects.all()
#     serializer_class=studentseializer
#     authentication_classes=[BasicAuthentication]
#     # permission_classes=[IsAuthenticated]
#     permission_classes=[IsAdminUser]


#  this is sessionAuthentication

class studentmodelview(viewsets.ModelViewSet):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    authentication_classes=[SessionAuthentication]
    
    permission_classes=[IsAuthenticated]
    permission_classes=[AllowAny]
    permission_classes=[IsAdminUser]
    permission_classes=[IsAuthenticatedOrReadOnly]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    
    
    # custom permission authentications
    # create my class to access permission used data
# class studentmodelview(viewsets.ModelViewSet):
#     queryset=Student1.objects.all()
#     serializer_class=studentseializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAdminUser]
#     permission_classes=[mypermission]
    
    
    
    