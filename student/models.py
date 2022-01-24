from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=30)
    department=models.CharField(max_length=20)
    cgpa=models.DecimalField(decimal_places=2,max_digits=5)

    def __str__(self):
        return self.name
