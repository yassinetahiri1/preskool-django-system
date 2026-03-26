from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_list, name='timetable_list'),
    path('add/', views.add_timetable, name='add_timetable'),
    path('delete/<int:pk>/', views.delete_timetable, name='delete_timetable'),
]