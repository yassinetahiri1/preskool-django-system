from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'category', 'uploaded_at')
    list_filter = ('category', 'subject')
    search_fields = ('title',)