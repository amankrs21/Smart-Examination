from .models import *
from exam.models import *
from student.models import *
from django.contrib import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='login')
def index(request):
    stud = StudentInfo.objects.count()
    dept = DepartmentInfo.objects.count()
    subj = SubjectInfo.objects.count()
    exam = ExamInfo.objects.count()
    ques = Questions.objects.count()
    resp = ExamResponse.objects.count()
    context = {
        'username':request.user,
        'stud':stud,
        'dept':dept,
        'subj':subj,
        'exam':exam,
        'ques':ques,
        'resp':resp,
    }
    return render(request, 'faculty/dashboard.html', context)


@login_required(login_url='login')
def AddDept(request):
    if request.method == 'GET':
        context = {
            'username':request.user
        }
        return render(request, 'faculty/AddDept.html', context)

    if request.method == 'POST':
        dep_name = request.POST['dep_name']
        dep_head = request.POST['dep_head']
        if DepartmentInfo.objects.filter(depname=dep_name).exists():
            messages.error(request, "Department Already Exist")
            return redirect('adddepartment')
        else:
            department = DepartmentInfo(depname=dep_name, dephead=dep_head)
            department.save()
            messages.success(request, "Department Added Succesfully.")
            return redirect('adddepartment')


@login_required(login_url='login')
def ViewDept(request):
    if request.method == 'GET':
        dept = DepartmentInfo.objects.all()
        context = {
            'username': request.user,
            "dept": dept,
        }
        return render(request, 'faculty/viewdept.html', context)


@login_required(login_url='login')
def ViewStud(request):
    if request.method == 'GET':
        stud = StudentInfo.objects.all()
        context = {
            'username': request.user,
            "stud": stud,
        }
        return render(request, 'faculty/viewstudent.html', context)


@login_required(login_url='login')
def ViewExam(request):
    if request.method == 'GET':
        exam = ExamInfo.objects.all()
        context = {
            'username': request.user,
            "exam": exam,
        }
        return render(request, 'faculty/viewexam.html', context)


@login_required(login_url='login')
def ViewSubj(request):
    if request.method == 'GET':
        subj = SubjectInfo.objects.all()
        context = {
            'username': request.user,
            "subj": subj,
        }
        return render(request, 'faculty/viewsubject.html', context)


@login_required(login_url='login')
def GenResult(request):
    if request.method == 'GET':
        resp = ExamResponse.objects.order_by().values('examname', 'student', 'studname',
                                                      'deptname', 'subjname', 'code').distinct()
        context = {
            'username': request.user,
            "resp": resp,
        }
        return render(request, 'faculty/genresult.html', context)


@login_required(login_url='login')
def ViewPaper(request, code):
    if request.method == 'GET':
        response = ExamResponse.objects.filter(code=code).values()
        context = {
            'username': request.user,
            "response": response,
        }
        return render(request, 'faculty/viewpaper.html', context)

    if request.method == 'POST':
        response = ExamResponse.objects.filter(code=code).values('question')
        for r in response:
            marks = request.POST['{}'.format(r['question'])]
            resp = ExamResponse.objects.get(question=r['question'])
            resp.marksgain = marks
            resp.save()

        response = ExamResponse.objects.filter(code=code).values()
        marks = 0
        total = 0
        for r in response:
            student = r['studname']
            examname = r['examname']
            deptname = r['deptname']
            subjname = r['subjname']
            marks = marks + r['marksgain']
            total = total + r['totalmarks']

        result = Result(code=code,student=student,examname=examname,deptname=deptname,subjname=subjname,totalmarks=total,marksgain=marks)
        result.save()
        messages.success(request, "Result Generated Successfull.")
        return redirect('generateresult')


@login_required(login_url='login')
def searchresult(request):
    if request.method == 'GET':
        result = Result.objects.all()
        context = {
            'username': request.user,
            'result': result,
        }
        return render(request, 'exam/searchresult.html', context)


@login_required(login_url='login')
def FacultyProfile(request):
    if request.method == 'GET':
        faculty = FacultyInfo.objects.get(user=request.user)
        context = {
            'username': request.user,
            'faculty':faculty,
        }
        return render(request, 'faculty/myprofile.html', context)
    
    if request.method == 'POST':
        name = request.POST['fullname']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']
        subject = request.POST['subject']
        address = request.POST['address']

        profile = FacultyInfo.objects.get(user=request.user)
        profile.name = name
        profile.email = email
        profile.number = phone
        profile.department = department
        profile.subject = subject
        profile.address = address
        profile.save()
        messages.success(request, "Profile Updated Successfully")
        return redirect('faculty')


@login_required(login_url='login')
def FacChangePass(request):
    if request.method == 'GET':
        context = {
            'username': request.user
        }
        return render(request, 'faculty/changepass.html', context)
    
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
            return redirect('faculty')
        else:
            messages.error(request, "Invalid Credentials :(")
            return redirect('facchangepass')
