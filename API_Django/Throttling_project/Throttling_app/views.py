from .models import Student1
from .seiliazer import studentseializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication,BaseAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny ,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

# this is basicAuthentication 

class studentmodelview(viewsets.ModelViewSet):
    queryset=Student1.objects.all()
    serializer_class=studentseializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    # permission_classes=[IsAdminUser]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]


