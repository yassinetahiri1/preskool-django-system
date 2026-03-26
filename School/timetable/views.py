from django.shortcuts import render, redirect, get_object_or_404
from .models import TimeTable
from Teacher.models import Teacher
from Subject.models import Subject

def timetable_list(request):
    context = {
        'schedules': TimeTable.objects.all(),
        'days': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
        'hours': [
            ('08:00', '08:00 AM - 10:00 AM'),
            ('10:00', '10:00 AM - 12:00 PM'),
            ('14:00', '02:00 PM - 04:00 PM'),
            ('16:00', '04:00 PM - 06:00 PM'),
        ],
    }
    return render(request, 'timetable/timetable.html', context)

def add_timetable(request):
    if request.method == "POST":
        TimeTable.objects.create(
            subject_id=request.POST.get('subject'),
            teacher_id=request.POST.get('teacher'),
            day=request.POST.get('day'),
            time_slot=request.POST.get('time_slot'),
            room=request.POST.get('room'),
            section=request.POST.get('section'),
        )
        return redirect('timetable_list')
    
    context = {
        'teachers': Teacher.objects.all(),
        'subjects': Subject.objects.all(),
    }
    return render(request, 'timetable/add-timetable.html', context)

def delete_timetable(request, pk):
    get_object_or_404(TimeTable, pk=pk).delete()
    return redirect('timetable_list')