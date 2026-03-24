from django.db import models
from Teacher.models import Teacher
from Departement.models import Department

class Subject(models.Model):
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    subject_id  = models.CharField(max_length=20, unique=True)
    name        = models.CharField(max_length=100)
    department  = models.ForeignKey(
                    Department,
                    on_delete=models.CASCADE,
                    related_name='subjects'
                  )
    teacher     = models.ForeignKey(
                    Teacher,
                    on_delete=models.SET_NULL,
                    null=True, blank=True,
                    related_name='subjects'
                  )
    description = models.TextField(blank=True)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return f"{self.name} ({self.subject_id})"