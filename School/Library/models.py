from django.db import models
from Subject.models import Subject

class Document(models.Model):
    CATEGORY_CHOICES = [
        ('Lesson', 'Lesson'),
        ('Exercise', 'Exercise'),
        ('Exam', 'Previous Exam'),
        ('Other', 'Other'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Lesson')
    file = models.FileField(upload_to='library/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.subject})"