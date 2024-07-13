from API_app.models import User
from API_app.api.seriliazer import userserializer
from rest_framework import viewsets

class userviewsite(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=userserializer