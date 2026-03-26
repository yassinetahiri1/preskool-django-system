from django.db import models
from Teacher.models import Teacher  
from Subject.models import Subject 

class TimeTable(models.Model):
    DAYS = [
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'),
    ]
    SLOTS = [
        ('08:00', '08:00 AM - 10:00 AM'),
        ('10:00', '10:00 AM - 12:00 PM'),
        ('14:00', '02:00 PM - 04:00 PM'),
        ('16:00', '04:00 PM - 06:00 PM'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.CharField(max_length=20, choices=DAYS)
    time_slot = models.CharField(max_length=20, choices=SLOTS)
    room = models.CharField(max_length=50)
    section = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.day} - {self.time_slot}"