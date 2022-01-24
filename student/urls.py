from django.urls import path
from . import views

urlpatterns=[
    path('studentDetails/',views.student_detail,name='studentDetail'),
    path('studentList/',views.student_list,name='studentList'),
    path('studentCreate/',views.student_create,name='studentCreate'),
    path('studentUpdate/',views.student_update,name='studentUpdate'),
    path('studentDelete/',views.student_delete,name='studentDelete'),
]