from django.db import models
from Teacher.models import Teacher
from Subject.models import Subject

class ClassTimeTable(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.class_name} - {self.section}"

class TimeTable(models.Model):
    DAYS = [
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'),
    ]
    SLOTS = [
        ('08:00', '08:00 - 10:00'),
        ('10:00', '10:00 - 12:00'),
        ('14:00', '14:00 - 16:00'),
        ('16:00', '16:00 - 18:00'),
    ]
    class_timetable = models.ForeignKey(ClassTimeTable, on_delete=models.CASCADE, related_name='slots')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAYS)
    time_slot = models.CharField(max_length=20, choices=SLOTS)
    room = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.class_timetable} | {self.day} - {self.time_slot}"