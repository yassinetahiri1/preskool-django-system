"""
URL configuration for School project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from home_auth.views import global_search # On importe la vue précise
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('faculty.urls')),
    path('student/', include('student.urls')),
    path('authentication/', include('home_auth.urls')), 
    path('Teacher/', include('Teacher.urls')), 
    path('Departement/', include('Departement.urls')),
    path('Subject/', include('Subject.urls')),
    path('Holidays/', include('Holidays.urls')),
    path('Exam/', include('Exam.urls')),
    path('Admin/', include('Admin.urls')),
    path('Event/', include('Events.urls')),
    path('timetable/', include('timetable.urls')),
    path('Library/', include('Library.urls')),
    path('search/', global_search, name='search_results'), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
