from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_api,name='StudentList'),
    path('<int:pk>/',views.get_api2,name='StudentDetails'),
]