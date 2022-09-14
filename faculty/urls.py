"""ses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
import ses.views as sesviews

urlpatterns = [
    path('', views.index, name='faculty'),
    path('login/', sesviews.LogoutView, name='logout'),
    path('adddepartment/', views.AddDept, name='adddepartment'),
    path('viewstudent/', views.ViewStud, name='viewstudent'),
    path('viewdepartment/', views.ViewDept, name='viewdepartment'),
    path('viewsubject/', views.ViewSubj, name='viewsubject'),
    path('viewexam/', views.ViewExam, name='view_exam'),
    path('generateresult/', views.GenResult, name='generateresult'),
    path('generateresult/viewpaper/<int:code>', views.ViewPaper, name="viewpaper"),
    path('viewresult/', views.searchresult, name="viewresult"),
    path('facultyprofile/', views.FacultyProfile, name="facultyprofile"),
    path('faculty-change-password/', views.FacChangePass, name='facchangepass'),
]
