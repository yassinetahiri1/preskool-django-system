from django.urls import path
from . import views

urlpatterns = [
    path('fees/', views.fees_list, name='fees_list'),
    path('fees/add/', views.add_fees, name='add_fees'),
    path('fees/delete/<int:fee_id>/', views.delete_fees, name='delete_fees'),

    path('expenses/', views.expenses_list, name='expenses_list'),
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/delete/<int:expense_id>/', views.delete_expense, name='delete_expense'),

    path('salary/', views.salary_list, name='salary_list'),
    path('salary/add/', views.add_salary, name='add_salary'),
    path('salary/delete/<int:salary_id>/', views.delete_salary, name='delete_salary'),
]