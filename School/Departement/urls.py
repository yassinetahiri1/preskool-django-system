from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.list,name='list'),
    path('Add',views.Add,name='Add'),
    path('Edit/<int:departement_id>/',views.Edit,name='Edit'),
    path('Delete/<int:departement_id>/', views.Delete, name='Delete'),
]
