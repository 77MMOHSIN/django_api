from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
     class  Meta:
          model=Student
          fields=['name','roll','city']
     # name=serializers.CharField(max_length=100)
     # roll=serializers.IntegerField()
     # city=serializers.CharField(max_length=12)
     # # data post
     # def create(self,validated_data):
     #      return Student.objects.create(** validated_data)
     # # data updated data
     # def update(self, instance, validated_data):
     #      instance.name=validated_data.get('name',instance.name)
     #      instance.roll=validated_data.get('roll',instance.roll)
     #      instance.city=validated_data.get('city',instance.city)
     #      instance.save()
     #      return instance
          

     
   