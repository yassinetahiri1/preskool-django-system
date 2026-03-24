from django.db import models

# Create your models here.
# Exam/models.py

from django.db import models
from Subject.models import Subject
from student.models import Student

class Exam(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    title       = models.CharField(max_length=200)
    subject     = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    exam_date   = models.DateField()
    start_time  = models.TimeField()
    end_time    = models.TimeField()
    student_class = models.CharField(max_length=50)
    section     = models.CharField(max_length=10)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Scheduled')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.subject} ({self.exam_date})"

class Result(models.Model):
    GRADE_CHOICES = [
        ('A+', 'A+'), ('A', 'A'),
        ('B+', 'B+'), ('B', 'B'),
        ('C+', 'C+'), ('C', 'C'),
        ('D', 'D'), ('F', 'F'),
    ]

    exam    = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks   = models.DecimalField(max_digits=5, decimal_places=2)
    total   = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    grade   = models.CharField(max_length=5, choices=GRADE_CHOICES, blank=True)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.exam} : {self.marks}/{self.total}"