from django.shortcuts import render,redirect
from student.models import Student
from Teacher.models import Teacher
from django.contrib.auth.decorators import login_required
from Subject.models import Subject
from Exam.models import Exam
from Holidays.models import Holiday

@login_required
def admin_dashboard(request):
    if not request.user.is_admin:
        return redirect('login')

    context = {
        'total_students': Student.objects.count(),
        'total_teachers': Teacher.objects.count(),
        'total_subjects': Subject.objects.count(),
        'total_exams': Exam.objects.count(),
        'total_holidays': Holiday.objects.count(),
        
        'recent_students': Student.objects.all().order_by('-id')[:5],
        'recent_teachers': Teacher.objects.all().order_by('-id')[:5],
        'upcoming_exams': Exam.objects.all().order_by('exam_date')[:5],
    }
    
    return render(request, 'Admin/admin-dashboard.html', context)