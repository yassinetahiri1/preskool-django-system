from django.shortcuts import render , redirect , get_object_or_404
from Teacher.models import Teacher
from Departement.models import Department
from .models import Subject
from django.contrib import messages

def add_subject(request):
    teachers = Teacher.objects.filter(status='Active')
    departments = Department.objects.filter(status='Active')

    if request.method == 'POST':
        Subject.objects.create(
            subject_id  = request.POST.get('subject_id'),
            name        = request.POST.get('name'),
            department  = Department.objects.get(id=request.POST.get('department')),
            teacher     = Teacher.objects.get(id=request.POST.get('teacher')) if request.POST.get('teacher') else None,
            description = request.POST.get('description'),
            status      = request.POST.get('status'),
        )
        return redirect('List')

    return render(request, 'Subject/Add.html', {'teachers': teachers,'departments': departments,})

def List(request):
    subjects = Subject.objects.all()
    return render(request,'Subject/List.html',{'subjects': subjects})

def Edit(request, id):
    subject = get_object_or_404(Subject, pk=id)
    teachers = Teacher.objects.filter(status='Active')
    departments = Department.objects.filter(status='Active')

    if request.method == 'POST':
        subject.subject_id  = request.POST.get('subject_id')
        subject.name        = request.POST.get('name')
        subject.department  = Department.objects.get(id=request.POST.get('department'))
        subject.teacher     = Teacher.objects.get(id=request.POST.get('teacher')) if request.POST.get('teacher') else None
        subject.description = request.POST.get('description')
        subject.status      = request.POST.get('status')
        subject.save()

        messages.success(request, 'Subject updated successfully')
        return redirect('List')

    return render(request, 'Subject/Edit.html', {'subject': subject,'teachers': teachers,'departments': departments,})

def Delete(request,id):
    Sub = get_object_or_404(Subject,id=id)
    Sub.delete()
    return redirect('List')