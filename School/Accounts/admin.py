from django.contrib import admin
from .models import FeesCollection, Expense, Salary

@admin.register(FeesCollection)
class FeesCollectionAdmin(admin.ModelAdmin):
    list_display = ('student', 'amount', 'payment_date', 'due_date', 'status')
    list_filter = ('status',)
    search_fields = ('student__first_name', 'student__last_name')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'date')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'amount', 'month', 'payment_date', 'status')
    list_filter = ('status', 'month')
    search_fields = ('teacher__first_name', 'teacher__last_name')