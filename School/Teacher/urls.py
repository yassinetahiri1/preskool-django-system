from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('teachers/',views.teacher_list,name='teacher_list'),
    path('teachers/add/',views.add_teacher,name='add_teacher'),
    path('teachers/edit/<int:teacher_id>/',views.edit_teacher,name='edit_teacher'),
    path('teachers/view/<int:teacher_id>/',views.view_teacher,name='view_teacher'),
    path('teachers/delete/<int:teacher_id>/',views.delete_teacher,name='delete_teacher'),
    path('dashboard/',views.dashboard,name='teacher-dashboard'),
]
