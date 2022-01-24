import io

from django.db.migrations import serializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import Student_serializer

@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stud_stream=io.BytesIO(json_data)
        stud_dictionary=JSONParser().parse(stud_stream)
        stud_seria=Student_serializer(data=stud_dictionary)

        if stud_seria.is_valid():
            stud_seria.save()
            response={'msg':'Student Created'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

def student_detail(request):
    if request.method=="GET":
        json_data = request.body
        stud_stream = io.BytesIO(json_data)
        stud_dictionary = JSONParser().parse(stud_stream)
        id = stud_dictionary.get('id')
        stud = Student.objects.get(id=id)
        stud_seria=Student_serializer(stud)
        stud_json=JSONRenderer().render(stud_seria.data)
        return HttpResponse(stud_json,content_type='application/json')

def student_list(request):
    if request.method=="GET":
        stud=Student.objects.all()
        stud_seria=Student_serializer(stud,many=True)
        stud_json=JSONRenderer().render(stud_seria.data)
        return HttpResponse(stud_json,content_type='application/json')

@csrf_exempt
def student_update(request):
    if request.method=='PUT':
        json_data=request.body
        stud_stream=io.BytesIO(json_data)
        stud_dictionary=JSONParser().parse(stud_stream)
        id=stud_dictionary.get('id')
        stud=Student.objects.get(id=id)
        stud_seria=Student_serializer(stud,data=stud_dictionary,partial=True)

        if stud_seria.is_valid():
            stud_seria.save()
            response={'msg':'Student Updated'}
            json_data=JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_delete(request):
    if request.method=='DELETE':
        json_data=request.body
        stud_stream=io.BytesIO(json_data)
        stud_dictionary=JSONParser().parse(stud_stream)
        id=stud_dictionary.get('id')
        stud=Student.objects.get(id=id)
        stud.delete()
        response={'msg':'Student Dleted'}
        json_data=JSONRenderer().render(response)
        return HttpResponse(json_data,content_type='application/json')