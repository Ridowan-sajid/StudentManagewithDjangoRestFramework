from rest_framework import serializers
from .models import Student

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    def validate_cgpa(self,value):
        if value>4.00:
           raise serializers.ValidationError("Cgpa cant be greater than 4")
        return value





