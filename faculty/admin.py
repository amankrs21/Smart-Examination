from django.contrib import admin

from faculty.models import FacultyInfo, DepartmentInfo

# Register your models here.
admin.site.register(FacultyInfo)
admin.site.register(DepartmentInfo)