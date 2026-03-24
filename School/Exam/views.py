from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Exam
from Subject.models import Subject
from .models import Result
from student.models import Student

def exam_list(request):
    exams = Exam.objects.all().order_by('exam_date')
    return render(request, 'Exam/exam-list.html', {'exams': exams})

def add_exam(request):
    subjects = Subject.objects.filter(status='Active')

    if request.method == 'POST':
        Exam.objects.create(
            title         = request.POST.get('title'),
            subject       = Subject.objects.get(id=request.POST.get('subject')),
            exam_date     = request.POST.get('exam_date'),
            start_time    = request.POST.get('start_time'),
            end_time      = request.POST.get('end_time'),
            student_class = request.POST.get('student_class'),
            section       = request.POST.get('section'),
            status        = request.POST.get('status'),
            description   = request.POST.get('description'),
        )
        messages.success(request, 'Exam added successfully')
        return redirect('exam_list')

    return render(request, 'Exam/add-exam.html', {'subjects': subjects})

def edit_exam(request, exam_id):
    exam     = get_object_or_404(Exam, pk=exam_id)
    subjects = Subject.objects.filter(status='Active')

    if request.method == 'POST':
        exam.title         = request.POST.get('title')
        exam.subject       = Subject.objects.get(id=request.POST.get('subject'))
        exam.exam_date     = request.POST.get('exam_date')
        exam.start_time    = request.POST.get('start_time')
        exam.end_time      = request.POST.get('end_time')
        exam.student_class = request.POST.get('student_class')
        exam.section       = request.POST.get('section')
        exam.status        = request.POST.get('status')
        exam.description   = request.POST.get('description')
        exam.save()

        messages.success(request, 'Exam updated successfully')
        return redirect('exam_list')

    return render(request, 'Exam/edit-exam.html', {
        'exam': exam,
        'subjects': subjects,
    })

def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    exam.delete()
    messages.success(request, 'Exam deleted successfully')
    return redirect('exam_list')


def exam_results(request):
    results = Result.objects.all().order_by('exam__exam_date')
    return render(request, 'Exam/exam-results.html', {'results': results})

def add_result(request):
    exams    = Exam.objects.filter(status='Completed')
    students = Student.objects.all()
    if request.method == 'POST':
        Result.objects.create(
            exam    = Exam.objects.get(id=request.POST.get('exam')),
            student = Student.objects.get(id=request.POST.get('student')),
            marks   = request.POST.get('marks'),
            total   = request.POST.get('total'),
            grade   = request.POST.get('grade'),
            remarks = request.POST.get('remarks'),
        )
        messages.success(request, 'Result added successfully')
        return redirect('exam_results')
    return render(request, 'Exam/add-result.html', {'exams': exams,'students': students})

def edit_result(request, result_id):
    result   = get_object_or_404(Result, pk=result_id)
    exams    = Exam.objects.filter(status='Completed')
    students = Student.objects.all()
    if request.method == 'POST':
        result.exam    = Exam.objects.get(id=request.POST.get('exam'))
        result.student = Student.objects.get(id=request.POST.get('student'))
        result.marks   = request.POST.get('marks')
        result.total   = request.POST.get('total')
        result.grade   = request.POST.get('grade')
        result.remarks = request.POST.get('remarks')
        result.save()
        messages.success(request, 'Result updated successfully')
        return redirect('exam_results')
    return render(request, 'Exam/edit-result.html', {'result': result,'exams': exams,'students': students,})

def delete_result(request, result_id):
    result = get_object_or_404(Result, pk=result_id)
    result.delete()
    messages.success(request, 'Result deleted successfully')
    return redirect('exam_results')