from django.db import models
from student.models import Student
from Teacher.models import Teacher

class FeesCollection(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.amount} ({self.status})"


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Utilities', 'Utilities'),
        ('Maintenance', 'Maintenance'),
        ('Supplies', 'Supplies'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.amount}"


class Salary(models.Model):
    STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
    ]
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='salaries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    month = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.teacher} - {self.amount} ({self.month})"