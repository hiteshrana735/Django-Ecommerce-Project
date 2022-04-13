from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def show(request):
    name = request.GET['name']
    password = request.GET['password']

    con = {
        'username' : name,
        'pass' : password
    }
    return render(request, 'show.html', con)