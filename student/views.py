import io
from django.db.migrations import serializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from .models import Student
from .serializers import Student_serializer

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def get_api(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            stu=Student.objects.get(id=pk)
            serializer=Student_serializer(stu)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            stu=Student.objects.all()
            serializer=Student_serializer(stu,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer = Student_serializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'student created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PATCH':
        stu = Student.objects.get(id=pk)
        serializer = Student_serializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'student updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='PUT':
        stu = Student.objects.get(id=pk)
        serializer = Student_serializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'student updated'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=='DELETE':
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response({'msg': 'student deleted'}, status=status.HTTP_200_OK)


