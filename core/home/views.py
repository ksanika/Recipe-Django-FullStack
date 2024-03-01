from django.shortcuts import render
from django.http import HttpResponse
from home.models import Course, Student


# Create your views here.

def home_func(request):
    course = Course(name="Python")
    course.save()

    student = Student(name="Rushikesh", course=course)
    student.save()

    students = Student.objects.all()

    return render(request, "index.html", context={'students': students})


def success_page(request):
    return HttpResponse("Success")
