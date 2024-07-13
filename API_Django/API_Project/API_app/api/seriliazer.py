from API_app.models import User

from rest_framework import serializers

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','name','email','password']