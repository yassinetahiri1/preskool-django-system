from django.shortcuts import render
from student.models import Student
from Teacher.models import Teacher
# Create your views here.

def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    return render(request,'Admin/admin-dashboard.html',{'teachers':teachers , 'students':students})