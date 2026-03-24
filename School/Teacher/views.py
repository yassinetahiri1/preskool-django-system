from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Teacher
from Exam.models import Exam
from Holidays.models import Holiday

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teachers.html', {'teachers': teachers})

def add_teacher(request):
    if request.method == 'POST':
        first_name        = request.POST.get('first_name')
        last_name         = request.POST.get('last_name')
        teacher_id        = request.POST.get('teacher_id')
        gender            = request.POST.get('gender')
        date_of_birth     = request.POST.get('date_of_birth')
        joining_date      = request.POST.get('joining_date')
        mobile_number     = request.POST.get('mobile_number')
        email             = request.POST.get('email')
        subject           = request.POST.get('subject')
        department        = request.POST.get('department')
        qualification     = request.POST.get('qualification')
        experience_years  = request.POST.get('experience_years')
        status            = request.POST.get('status')
        present_address   = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        teacher_image     = request.FILES.get('teacher_image')

        Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            teacher_id=teacher_id,
            gender=gender,
            date_of_birth=date_of_birth,
            joining_date=joining_date,
            mobile_number=mobile_number,
            email=email,
            subject=subject,
            department=department,
            qualification=qualification,
            experience_years=experience_years,
            status=status,
            present_address=present_address,
            permanent_address=permanent_address,
            teacher_image=teacher_image,
        )
        messages.success(request, 'Teacher added successfully')
        return redirect('teacher_list')
    else:
        return render(request, 'teachers/add-teacher.html')


def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.first_name       = request.POST.get('first_name')
        teacher.last_name        = request.POST.get('last_name')
        teacher.teacher_id       = request.POST.get('teacher_id')
        teacher.gender           = request.POST.get('gender')
        teacher.date_of_birth    = request.POST.get('date_of_birth')
        teacher.joining_date     = request.POST.get('joining_date')
        teacher.mobile_number    = request.POST.get('mobile_number')
        teacher.email            = request.POST.get('email')
        teacher.subject          = request.POST.get('subject')
        teacher.department       = request.POST.get('department')
        teacher.qualification    = request.POST.get('qualification')
        teacher.experience_years = request.POST.get('experience_years')
        teacher.status           = request.POST.get('status')
        teacher.present_address  = request.POST.get('present_address')
        teacher.permanent_address = request.POST.get('permanent_address')

        if request.FILES.get('teacher_image'):
            teacher.teacher_image = request.FILES.get('teacher_image')

        teacher.save()
        messages.success(request, 'Teacher updated successfully')
        return redirect('teacher_list')

    return render(request, 'teachers/edit-teacher.html', {'teacher': teacher})


def view_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id) 
    return render(request, 'teachers/teacher-details.html', {'teacher': teacher})


def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    teacher.delete()
    messages.success(request, 'Teacher deleted successfully')
    return redirect('teacher_list')

def dashboard(request):
    exams = Exam.objects.all()
    holidays = Holiday.objects.all()
    return render(request,'teachers/teacher-dashboard.html' , {'exams':exams , 'holidays':holidays})