from django.shortcuts import render , redirect , get_object_or_404 
from .models import Department
from Teacher.models import Teacher
from django.contrib import messages
# Create your views here.

def list(request):
    Departments = Department.objects.all()
    return render(request,'Departement/List.html',{'departments':Departments})

def Add(request):
    Teachers = Teacher.objects.all()
    if request.method == 'POST':
        department_id = request.POST.get('department_id')
        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        Departments = Department(department_id = department_id , name = name , description = description , status = status)
        Departments.save()
        return redirect('list')
    return render(request,'Departement/Add.html',{'teachers':Teachers})

def Edit(request,departement_id):
    Departements = get_object_or_404(Department,pk=departement_id)
    Teachers = Teacher.objects.all()
    if request.method == 'POST':
        Departements.deparetement_id = request.POST.get('Departement_id')
        Departements.name = request.POST.get('name')
        Departements.description = request.POST.get('description')
        Departements.status = request.POST.get('status')
        Departements.save()

        selected_teachers = request.POST.getlist('teachers')
        Departements.teachers.set(selected_teachers) 

        messages.success(request, 'Department updated successfully')
        return redirect('list')

    return render(request, 'Departement/Edit.html', {'department': Departements,'teachers': Teachers,})

def Delete(request, departement_id):
    department = get_object_or_404(Department, pk=departement_id)
    department.delete()
    messages.success(request, 'Department deleted successfully')
    return redirect('list')