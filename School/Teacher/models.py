from django.db import models

# Create your models here.
class Teacher(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    STATUS_CHOICES = [('Active', 'Active'), ('Inactive', 'Inactive')]

    # Informations personnelles
    first_name        = models.CharField(max_length=100)
    last_name         = models.CharField(max_length=100)
    teacher_id        = models.CharField(max_length=20, unique=True)
    gender            = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth     = models.DateField()
    joining_date      = models.DateField()
    mobile_number     = models.CharField(max_length=15)
    email             = models.EmailField(max_length=100, unique=True)
    teacher_image     = models.ImageField(upload_to='teachers/', blank=True)

    # Informations professionnelles
    subject           = models.CharField(max_length=100)   # ex: Mathématiques
    department        = models.CharField(max_length=100)   # ex: Sciences
    qualification     = models.CharField(max_length=100)   # ex: Master, Doctorat
    experience_years  = models.PositiveIntegerField(default=0)
    status            = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    # Adresse
    present_address   = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.teacher_id})"