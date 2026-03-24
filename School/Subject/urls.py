from django.contrib import admin
from django.urls import path , include
from . import views
urlpatterns = [
    path('Add/',views.add_subject , name='add_subject'),
    path('List/',views.List , name='List'),
    path('Edit/<int:id>/',views.Edit , name='EditS'),
    path('Delete/<int:id>/',views.Delete , name='DeleteS'),
]
