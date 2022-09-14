from exam.models import *
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StudentInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=12, blank=True)
    department = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Student Info'


class ExamResponse(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, null=True)
    code = models.IntegerField(blank=True, null=True)
    studname = models.CharField(max_length=50, blank=True, null=True)
    deptname = models.CharField(max_length=50, blank=True, null=True)
    subjname = models.CharField(max_length=50, blank=True, null=True)
    examname = models.CharField(max_length=100, blank=True, null=True)
    question = models.CharField(max_length=500, blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    totalmarks = models.IntegerField(blank=True, null=True)
    marksgain = models.IntegerField(blank=True, null=True)

    # def __str__(self):
    #     return self.student

    class Meta:
        verbose_name_plural = 'Exam Response'


class StuExamHistory(models.Model):
    student = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    examname = models.CharField(max_length=100, blank=True)
    appeareddate = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=50, blank=True)
    totalmarks = models.IntegerField(blank=True)

    class Meta:
        verbose_name_plural = 'Student Exam History'