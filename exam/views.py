from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def AddSubject(request):
    if request.method == 'GET':
        form = SubjectForm()
        return render(request, 'exam/AddSubject.html', {'myform':form})

    if request.method == 'POST':
        form = SubjectForm(request.POST)
        sub_name = request.POST['subjectname']
        if SubjectInfo.objects.filter(subjectname=sub_name).exists():
            messages.error(request, "Subject Already Exist")
            return redirect('addsubject')
        else:
            if form.is_valid():
                form.save()
            messages.success(request, "Subject Added Successfully")
            return redirect('addsubject')


@login_required(login_url='login')
def AddExam(request):
    if request.method == 'GET':
        form = ExamForm()
        return render(request, 'exam/AddExam.html', {'myform':form})

    if request.method ==  'POST':
        form = ExamForm(request.POST)
        examname = request.POST['exam_name']
        examdept = request.POST['examdept']
        examsubj = request.POST['examsubj']
        starttime = request.POST['starttime']
        infoexam = str(examdept+" "+examname+" "+examsubj+" "+starttime[:10])
        prof = request.user
        # prof_user = User.objects.get(username=prof)
        if ExamInfo.objects.filter(examname=infoexam).exists():
            messages.error(request, "Exam Already Exist")
            return redirect('addexam')
        else:
            if form.is_valid():
                exam = form.save(commit=False)
                exam.facultyname = prof
                exam.examname = infoexam
                exam.save()
                form.save_m2m()
                messages.success(request, "Exam Added Successfully")
                return redirect('addexam')
            else:
                messages.error(request, "Error while adding exam")
                return redirect('addexam')



@login_required(login_url='login')
def Objective(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'exam/AddObject.html', {'myform':form})

    if request.method ==  'POST':
        option = request.POST['correct_ans']
        form = QuestionForm(request.POST)
        question = request.POST['question']
        examname = request.POST['examname']
        if Questions.objects.filter(question=question, examname=examname).exists():
            messages.error(request, "Question Already Exist")
            return redirect('addobjective')
        else:
            if option == '1':
                ansr = request.POST['option1']
            elif option == '2':
                ansr = request.POST['option2']
            elif option == '3':
                ansr = request.POST['option3']
            elif option == '4':
                ansr = request.POST['option4']
            else:
                ansr = ' '
            if form.is_valid():
                quest = form.save(commit=False)
                quest.question_type = "Objective"
                quest.answer = ansr
                quest.save()
                form.save_m2m()
                messages.success(request, "Question Added Successfully")
                return redirect('addobjective')
            else:
                messages.error(request, "Error while adding question")
                return redirect('addobjective')


@login_required(login_url='login')
def Subjective(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'exam/AddSubj.html', {'myform':form})

    if request.method ==  'POST':
        form = QuestionForm(request.POST)
        question = request.POST['question']
        examname = request.POST['examname']
        if Questions.objects.filter(question=question, examname=examname).exists():
            messages.error(request, "Question Already Exist")
            return redirect('addsubjective')
        else:
            if form.is_valid():
                quest = form.save(commit=False)
                quest.question_type = "Subjective"
                quest.answer = " "
                quest.save()
                form.save_m2m()
                messages.success(request, "Question Added Successfully")
                return redirect('addsubjective')
            else:
                messages.error(request, "Error while adding question")
                return redirect('addsubjective')


@login_required(login_url='login')
def Coding(request):
    if request.method == 'GET':
        form = QuestionForm()
        return render(request, 'exam/AddCoding.html', {'myform':form})

    if request.method ==  'POST':
        form = QuestionForm(request.POST)
        question = request.POST['question']
        examname = request.POST['examname']
        if Questions.objects.filter(question=question, examname=examname).exists():
            messages.error(request, "Question Already Exist")
            return redirect('addcoding')
        else:
            if form.is_valid():
                quest = form.save(commit=False)
                quest.question_type = "Coding"
                quest.answer = " "
                quest.save()
                form.save_m2m()
                messages.success(request, "Question Added Successfully")
                return redirect('addcoding')
            else:
                messages.error(request, "Error while adding question")
                return redirect('addcoding')

