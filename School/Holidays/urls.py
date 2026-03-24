from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.holidays,name='Holidays'),
    path('Add/',views.Add,name='Add'),
    path('Edit/<int:id>/',views.Edit,name='Edit'),
    path('Delete/<int:id>/',views.Delete,name='Delete'),
]