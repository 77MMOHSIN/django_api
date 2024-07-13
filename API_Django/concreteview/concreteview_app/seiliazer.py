from rest_framework import serializers
from .models import Student1
class studentseializer(serializers.ModelSerializer):
    class Meta:
        model= Student1
        fields=['id','name','roll','city']
