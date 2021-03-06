from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import Student_serializer

@api_view(['GET','POST'])
def get_api(request):
    if request.method=='GET':
        stu=Student.objects.all()
        serializer=Student_serializer(stu,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method=='POST':
        serializer = Student_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'student created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH','PUT','DELETE'])
def get_api2(request,pk):

    if request.method=='GET':
        stu=Student.objects.get(id=pk)
        serializer=Student_serializer(stu)
        return Response(serializer.data, status=status.HTTP_200_OK)

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

