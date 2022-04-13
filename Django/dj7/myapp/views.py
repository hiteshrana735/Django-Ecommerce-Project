from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST['name']
        useremail = request.POST['email']
        userpassword = request.POST['password']
        userpassword2 = request.POST['password2']

        if userpassword == userpassword2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('')

            elif User.objects.filter(email=useremail).exists():
                messages.info(request, "Email already in Use")
                return redirect('')

            else:
                newuser = User.objects.create_user(username=username, email=useremail, password=userpassword)
                newuser.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('')
    return render(request, 'index.html')


def show(request):
    users = User.objects.all()
    return render(request, 'show.html', {'details': users})

def login(request):
    if request.method == 'POST':
        username = request.POST['name']
        userpassword = request.POST['password']

        user = auth.authenticate(username=username, password=userpassword)

        if user is None:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
        else:
            auth.login(request, user)
            return redirect('dashboard')
            
    return render(request, 'login.html')

def dash(request):
    return render(request, 'dashboard.html')

def logout(request):
    auth.logout(request)
    return redirect("")




""" 
MVT
Get and POST
Dynamic data
Dynamic data with model
Dynamic data from API
User Management
ORM
REST Api
Project
"""