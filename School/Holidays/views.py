from django.shortcuts import render , redirect , get_object_or_404
from .models import Holiday
from django.contrib import messages
# Create your views here.

def holidays(request):
    holidays = Holiday.objects.all()
    return render(request,'Holidays/holidays.html',{'Holidays':holidays})

def Add(request):
    if request.method == 'POST':
        Holiday.objects.create(
            title       = request.POST.get('title'),
            start_date  = request.POST.get('start_date'),
            end_date    = request.POST.get('end_date'),
            description = request.POST.get('description'),
        )
        messages.success(request, 'Holiday added successfully')
        return redirect('Holidays')
    return render(request, 'Holidays/Add.html')

def Edit(request , id):
    holiday = get_object_or_404(Holiday,id=id)
    if request.method == 'POST':
        holiday.title = request.POST.get('title')
        holiday.start_date = request.POST.get('start_date')
        holiday.end_date = request.POST.get('end_date')
        holiday.description = request.POST.get('description')
        holiday.save()
        messages.success(request,'Holiday modified successfully')
        return redirect('Holidays')
    return render(request,'Holidays/Edit.html',{'holiday':holiday})

def Delete(request,id):
    holiday = get_object_or_404(Holiday,id=id)
    holiday.delete()
    return redirect('Holidays')