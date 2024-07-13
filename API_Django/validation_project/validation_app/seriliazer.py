from rest_framework import serializers
from .models import Student



# validators
def start_with_r(value):
     if value[0].lower()!='r':
          raise serializers.ValidationError('Name should be start with R')
     
class StudentSerializer(serializers.Serializer):
     
     name=serializers.CharField(max_length=100,validators=[start_with_r])
     roll=serializers.IntegerField()
     city=serializers.CharField(max_length=12)
     # data post
     def create(self,validated_data):
          return Student.objects.create(** validated_data)
     # data updated data
     def update(self, instance, validated_data):
          instance.name=validated_data.get('name',instance.name)
          instance.roll=validated_data.get('roll',instance.roll)
          instance.city=validated_data.get('city',instance.city)
          instance.save()
          return instance
     # field label validation
     def validate_roll(self, value):
          if value>=200:
               raise serializers.ValidationError(' seat full')
          return value
     # object level validation
     def validate(self, data):
          nm=data.get('name')
          ct=data.get('city')
          if nm.lower()=='moshin' and ct.lower() !='jamalpur':
               raise serializers.ValidationError(' city must be jamal[pur]')
          return data
     
          
          

     
   