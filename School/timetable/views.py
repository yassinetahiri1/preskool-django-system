from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import ClassTimeTable, TimeTable
from Teacher.models import Teacher
from Subject.models import Subject

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
HOURS = [
    ('08:00', '08:00 - 10:00'),
    ('10:00', '10:00 - 12:00'),
    ('14:00', '14:00 - 16:00'),
    ('16:00', '16:00 - 18:00'),
]

def timetable_home(request):
    classes = ClassTimeTable.objects.all()
    return render(request, 'timetable/timetable_home.html', {'classes': classes})

def create_class_timetable(request):
    if request.method == 'POST':
        class_name = request.POST.get('class_name').strip()
        section = request.POST.get('section').strip()
        ct = ClassTimeTable.objects.create(class_name=class_name, section=section)
        messages.success(request, f'Timetable for {class_name} created.')
        return redirect('timetable_detail', pk=ct.pk)
    return render(request, 'timetable/create_class.html')

def timetable_detail(request, pk):
    ct = get_object_or_404(ClassTimeTable, pk=pk)
    slots = ct.slots.all()
    return render(request, 'timetable/timetable.html', {
        'ct': ct,
        'slots': slots,
        'days': DAYS,
        'hours': HOURS,
        'teachers': Teacher.objects.all(),
        'subjects': Subject.objects.all(),
    })

def add_slot(request, pk):
    ct = get_object_or_404(ClassTimeTable, pk=pk)
    if request.method == 'POST':
        TimeTable.objects.create(
            class_timetable=ct,
            subject_id=request.POST.get('subject'),
            teacher_id=request.POST.get('teacher'),
            day=request.POST.get('day'),
            time_slot=request.POST.get('time_slot'),
            room=request.POST.get('room'),
        )
        messages.success(request, 'Slot added.')
    return redirect('timetable_detail', pk=pk)

def delete_slot(request, pk):
    slot = get_object_or_404(TimeTable, pk=pk)
    ct_pk = slot.class_timetable.pk
    slot.delete()
    return redirect('timetable_detail', pk=ct_pk)

def delete_class_timetable(request, pk):
    ct = get_object_or_404(ClassTimeTable, pk=pk)
    ct.delete()
    messages.success(request, 'Timetable deleted.')
    return redirect('timetable_home')