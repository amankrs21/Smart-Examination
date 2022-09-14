from django.contrib import auth
from django.contrib import messages
from student.models import StudentInfo
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # has_grp = False

        if username and password:
            user = auth.authenticate(username=username,password=password)
            exis = User.objects.filter(username=username).exists()

            if exis:
                user_ch = User.objects.get(username=username)
                # has_grp = has_group(user_ch,"Professor")

            if user and user.is_active and exis and user_ch.is_staff:
                auth.login(request,user)
                messages.success(request,"Welcome, "+ user.username + ". You are now logged in.")
                return redirect('faculty')

            if user and user.is_active and exis and not user_ch.is_staff:
                auth.login(request,user)
                # messages.success(request,"Welcome, "+ user.username + ". You are now logged in.")
                return redirect('student')
                
            # elif user and exis and user_ch.is_staff and not has_grp:
            #     messages.error(request,'You dont have permssions to login as faculty. Please contact Admin')
            #     return redirect('login')

            else:
                messages.error(request,'Invalid credentials :(')
                return redirect('login')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['pass']
        name = request.POST['name']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username Already Exist")
            return redirect('register')
        
        else:
            student = User(username=username, email=email)
            student.set_password(password)
            student.save()

            stu_info = StudentInfo(name=name)
            stu_info.user = student
            stu_info.save()

            messages.success(request,"Registered Succesfully!!")
            return redirect('login')


def LogoutView(request):
    auth.logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('login')