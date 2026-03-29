from django.contrib import admin
from .models import ClassTimeTable, TimeTable

@admin.register(ClassTimeTable)
class ClassTimeTableAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section')

@admin.register(TimeTable)
class TimeTableAdmin(admin.ModelAdmin):
    list_display = ('class_timetable', 'subject', 'teacher', 'day', 'time_slot', 'room')