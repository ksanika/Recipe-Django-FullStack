from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=10)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
