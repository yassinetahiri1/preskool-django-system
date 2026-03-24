from django.db import models
from Teacher.models import Teacher

class Department(models.Model):
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    department_id  = models.CharField(max_length=20, unique=True)
    name           = models.CharField(max_length=100)
    description    = models.TextField(blank=True)

    teachers       = models.ManyToManyField(Teacher,blank=True,related_name='departments')

    status         = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    created_at     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.department_id})"