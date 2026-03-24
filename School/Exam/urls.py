from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('Add/', views.add_exam, name='add_exam'),
    path('Edit/<int:exam_id>/', views.edit_exam, name='edit_exam'),
    path('Delete/<int:exam_id>/', views.delete_exam, name='delete_exam'),
    path('Results/', views.exam_results, name='exam_results'),
    path('Results/Add/', views.add_result, name='add_result'),
    path('Results/Edit/<int:result_id>/', views.edit_result, name='edit_result'),
    path('Results/Delete/<int:result_id>/', views.delete_result, name='delete_result'),
]