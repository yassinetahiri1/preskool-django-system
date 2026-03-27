from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Document
from Subject.models import Subject

def library_home(request):
    subjects = Subject.objects.all()
    return render(request, 'Library/library.html', {'subjects': subjects})

def subject_documents(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    documents = Document.objects.filter(subject=subject)
    categories = ['Lesson', 'Exercise', 'Exam', 'Other']
    return render(request, 'Library/subject_documents.html', {
        'subject': subject,
        'documents': documents,
        'categories': categories,
    })

def add_document(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        file = request.FILES.get('file')
        Document.objects.create(
            subject=subject,
            title=title,
            category=category,
            file=file
        )
        messages.success(request, 'Document added successfully')
        return redirect('subject_documents', subject_id=subject_id)
    return render(request, 'Library/add_document.html', {'subject': subject})

def delete_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    subject_id = doc.subject.id
    doc.file.delete()
    doc.delete()
    messages.success(request, 'Document deleted successfully')
    return redirect('subject_documents', subject_id=subject_id)