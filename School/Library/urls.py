from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home, name='library_home'),
    path('subject/<int:subject_id>/', views.subject_documents, name='subject_documents'),
    path('add/<int:subject_id>/', views.add_document, name='add_document'),
    path('delete/<int:doc_id>/', views.delete_document, name='delete_document'),
]