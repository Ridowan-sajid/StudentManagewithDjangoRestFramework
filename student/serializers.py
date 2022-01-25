from rest_framework import serializers
from .models import Student

class Student_serializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

    # def validate_cgpa(self,value):
    #     if value>4.00:
    #        raise serializers.ValidationError("Cgpa cant be greater than 4")
    #     return value

    def validate(self, attrs):
        cg=attrs.get('cgpa')
        if cg > 4.00:
            raise serializers.ValidationError("Cgpa cant be greater than 4")
        return attrs



# class Student_serializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     department = serializers.CharField(max_length=20)
#     cgpa = serializers.DecimalField(decimal_places=3, max_digits=5)
#
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)
#         instance.department=validated_data.get('department',instance.department)
#         instance.cgpa=validated_data.get('cgpa',instance.cgpa)
#         instance.save()
#         return instance
