from statistics import mode
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FacultyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=12, blank=True)
    department = models.CharField(max_length=12, blank=True)
    subject = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Faculty Info'


class DepartmentInfo(models.Model):
    depname = models.CharField(max_length=50, blank=True, primary_key=True)
    dephead = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.depname

    class Meta:
        verbose_name_plural = 'Department Info'