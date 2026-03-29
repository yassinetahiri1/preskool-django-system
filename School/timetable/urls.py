from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_home, name='timetable_home'),
    path('create/', views.create_class_timetable, name='create_class_timetable'),
    path('class/<int:pk>/', views.timetable_detail, name='timetable_detail'),
    path('class/<int:pk>/add-slot/', views.add_slot, name='add_slot'),
    path('slot/delete/<int:pk>/', views.delete_slot, name='delete_slot'),
    path('class/delete/<int:pk>/', views.delete_class_timetable, name='delete_class_timetable'),
]