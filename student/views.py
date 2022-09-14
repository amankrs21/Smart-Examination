import random
from .models import *
from exam.models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')


def index(request):
    exam = ExamInfo.objects.count()
    names = StudentInfo.objects.get(user=request.user)
    result = Result.objects.filter(student=names.name).count()
    return render(request, 'student/dashboard.html', {'exam':exam,'result':result})


def ViewExam(request):
    info = StudentInfo.objects.get(user=request.user)
    exam = ExamInfo.objects.all()
    history = StuExamHistory.objects.get(student=info)
    context = {
        'exam':exam,
        'history':history,
    }
    
    return render(request, 'student/viewexam.html', context)


def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    min += hour*60
    return "%02d:%02d" % (min, sec)


def AppearExam(request, id):
    exam = ExamInfo.objects.get(pk=id)
    if request.method == 'GET':
        exam_name = exam.examname
        quest = Questions.objects.filter(examname__examname__contains=exam_name).values()
        time_delta = exam.endtime - exam.starttime
        time = convert(time_delta.seconds)
        time = time.split(":")
        mins = time[0]
        secs = time[1]
        context = {
            "exam": exam,
            "quest": quest,
            "sec": secs,
            "min": mins
        }
        return render(request, 'student/exam.html', context)

    if request.method == 'POST':
        exam_name = request.POST['paper']
        questions = Questions.objects.filter(examname__examname__contains=exam_name).values()
        stud = StudentInfo.objects.filter(user=request.user).values()
        code = int(random.random() * 100000)
        for n in stud:
            name = n['name']
        for q in questions:
            examres = ExamResponse(code=code,studname=name,examname=exam_name,deptname=exam.examdept,subjname=exam.examsubj,question=q['question'],totalmarks=q['marks'])
            if q['question_type'] == 'Objective':
                ans = request.POST['{}'.format(q['question'])]
                if q['answer'] == ans:
                    marks = q['marks']
                else:
                    marks = 0
                
            else:
                ans = request.POST['{}'.format(q['question'])]
                marks = 0

            examres.student = StudentInfo.objects.get(user=request.user)
            examres.answer = ans
            examres.marksgain = marks
            examres.save()

        history = StuExamHistory(examname=exam_name,subject=exam.examsubj,appeareddate=exam.starttime,totalmarks=exam.totalmarks)
        history.student = StudentInfo.objects.get(user=request.user)
        history.save()

        messages.success(request, "Your Exam is Submited Successfully .")
        return redirect('viewexam')


def ViewResult(request):
    stud = StudentInfo.objects.filter(user=request.user).values()
    for n in stud:
        name = n['name']
    sturesult = Result.objects.filter(student=name).values()
    context = {
        'result':sturesult,
    }
    return render(request, 'student/viewresult.html', context)


def ViewResponse(request, code):
    response = ExamResponse.objects.filter(code=code).values()
    context = {
        'response':response,
    }
    return render(request, 'student/viewresponse.html', context)


def ExamHistory(request):
    stud = StudentInfo.objects.get(user=request.user)
    response = StuExamHistory.objects.filter(student=stud).values()
    context = {
        'response':response,
    }
    return render(request, 'student/examhistory.html', context)


def MyProfile(request):
    if request.method == 'GET':
        stud = StudentInfo.objects.get(user=request.user)
        context = {
            'stud':stud,
        }
        return render(request, 'student/myprofile.html', context)

    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        address = request.POST['address']

        profile = StudentInfo.objects.get(user=request.user)
        profile.name = name
        profile.email = email
        profile.number = phone
        profile.department = department
        profile.address = address
        profile.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('student')

def StuChangePassword(request):
    if request.method == 'GET':
        return render(request, 'student/changepass.html')
    
    if request.method == 'POST':
        oldpass = request.POST['oldpass']
        newpass = request.POST['newpass']
        userinfo = auth.authenticate(username=request.user,password=oldpass)
        users=User.objects.filter(username=request.user)
        user=users[0]
        if userinfo:
            user.set_password = newpass
            user.save()
            messages.success(request, "Password Changed Successfully")
            return redirect('student')
        else:
            messages.error(request, "Invalid Credentials :(")
            return redirect('stuchangepass')