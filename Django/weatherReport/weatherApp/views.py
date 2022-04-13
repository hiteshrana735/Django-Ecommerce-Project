from django.shortcuts import render, redirect
import urllib 
import json
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        search_city = request.POST['city_name']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + search_city + '&appid=0b892f82700f99d1bc0c154a4f756cea&units=metric').read()

        list_of_data = json.loads(source)

        context = {
            "city_name" : search_city,
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']) + 'degree C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']), 
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
        }

        return render(request, 'result.html', context)

    
    else :
        return render(request, 'result.html')

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
            return redirect('home')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        useremail = request.POST['email']
        userpassword = request.POST['password']
        userpassword2 = request.POST['password2']

        if userpassword == userpassword2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register')

            elif User.objects.filter(email=useremail).exists():
                messages.info(request, "Email already in Use")
                return redirect('register')

            else:
                newuser = User.objects.create_user(username=username, email=useremail, password=userpassword)
                newuser.save()
                return redirect('login')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    return render(request, 'register.html')