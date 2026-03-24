from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from django.contrib import messages

def event_list(request):
    events = Event.objects.all().order_by('-start_date')
    return render(request, 'events/event_list.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        category = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        location = request.POST.get('location')
        description = request.POST.get('description')

        Event.objects.create(
            title=title, category=category, start_date=start_date,
            end_date=end_date, location=location, description=description
        )
        messages.success(request, "L'événement a été ajouté !")
        return redirect('event_list')
    return render(request, 'events/add_event.html')

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.category = request.POST.get('category')
        event.start_date = request.POST.get('start_date')
        event.end_date = request.POST.get('end_date')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        event.save()
        messages.success(request, "Événement mis à jour !")
        return redirect('event_list')
    return render(request, 'events/edit_event.html', {'event': event})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.success(request, "Événement supprimé.")
    return redirect('event_list')