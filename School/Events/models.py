from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Holiday', 'Holiday'),
        ('Sports', 'Sports'),
        ('Others', 'Others'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Academic')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title