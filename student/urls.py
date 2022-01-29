from django.urls import path
from . import views

urlpatterns=[
    path('studentList/',views.get_api,name='StudentList'),
    path('studentList/<int:pk>',views.get_api,name='StudentDetails'),
]