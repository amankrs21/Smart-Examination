from datetime import datetime
from django import forms
from django.db import models
from django.forms import ModelForm
from faculty.models import DepartmentInfo
import student

# Create your models here.
class SubjectInfo(models.Model):
    subjectname = models.CharField(max_length=100, blank=True, primary_key=True)
    subjectcode = models.IntegerField(null=True)

    def __str__(self):
        return self.subjectname

    class Meta:
        verbose_name_plural = 'Subject Info'

class SubjectForm(ModelForm):
    class Meta:
        model = SubjectInfo
        fields = ['subjectname', 'subjectcode']
        widgets = {
            'subjectname': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'Subject Name','required':'True'}),
            'subjectcode': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'Subject Code','required':'True'}),
        }
        labels = {
            'subjectname': '',
            'subjectcode': '',
        }


class ExamInfo(models.Model):
    examdept = models.ForeignKey(DepartmentInfo, on_delete=models.CASCADE, null=True)
    examsubj = models.ForeignKey(SubjectInfo, on_delete=models.CASCADE, null=True)
    examname = models.CharField(max_length=100, blank=True)
    facultyname = models.CharField(max_length=50, blank=True)
    totalmarks = models.IntegerField(blank=True)
    starttime = models.DateTimeField(default=datetime.now())
    endtime = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.examname
    
    class Meta:
        verbose_name_plural = 'Exam Info'
    
class ExamForm(ModelForm):
    class Meta:
        model = ExamInfo
        fields = ['examdept', 'examsubj', 'totalmarks', 'starttime', 'endtime']
        labels = {
            'examdept':'',
            'examsubj':'',
            'totalmarks':'',
        }
        widgets = {
            'totaltime': forms.NumberInput(attrs = {'class':'time', 'placeholder':'Time(in mm)','required':'True'}),
            'totalmarks': forms.NumberInput(attrs = {'class':'marks', 'placeholder':'Marks','required':'True'}),
        }


class Questions(models.Model):
    examname = models.ForeignKey(ExamInfo, on_delete=models.CASCADE, null=True)
    question_type = models.CharField(max_length=50, blank=True)
    question = models.TextField(max_length=1000, blank=True)
    option1 = models.CharField(max_length=500, blank=True, null=True)
    option2 = models.CharField(max_length=500, blank=True, null=True)
    option3 = models.CharField(max_length=500, blank=True, null=True)
    option4 = models.CharField(max_length=500, blank=True, null=True)
    answer = models.CharField(max_length=500, blank=True)
    marks = models.IntegerField(blank=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = 'Questions'

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['examname', 'question_type', 'question', 'option1', 'option2', 'option3', 'option4', 'answer', 'marks']
        labels = {
            'examname':'',
            'question_type':'',
            'question':'',
            'option1':'',
            'option2':'',
            'option3':'',
            'option4':'',
            'answer':'',
            'marks':'',
        }
        widgets = {
            'question': forms.Textarea(attrs = {'class':'textarea-question', 'rows':'5', 'placeholder':'Write the question here...', 'required':'True'}),
            'option1': forms.Textarea(attrs = {'class':'textarea-option', 'rows':'1', 'placeholder':'Option 1', 'required':'True'}),
            'option2': forms.Textarea(attrs = {'class':'textarea-option', 'rows':'1', 'placeholder':'Option 2', 'required':'True'}),
            'option3': forms.Textarea(attrs = {'class':'textarea-option', 'rows':'1', 'placeholder':'Option 3', 'required':'True'}),
            'option4': forms.Textarea(attrs = {'class':'textarea-option', 'rows':'1', 'placeholder':'Option 4', 'required':'True'}),
            'marks': forms.NumberInput(attrs = {'class':'marks', 'placeholder':'Marks','required':'True'}),
        }


class Result(models.Model):
    code = models.IntegerField(blank=True)
    student = models.CharField(max_length=100, blank=True)
    examname = models.CharField(max_length=100, blank=True)
    deptname = models.CharField(max_length=50, blank=True)
    subjname = models.CharField(max_length=50, blank=True)
    totalmarks = models.IntegerField(blank=True)
    marksgain = models.IntegerField(blank=True)
    grade = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.examname+" "+self.student
    
    class Meta:
        verbose_name_plural = 'Result'