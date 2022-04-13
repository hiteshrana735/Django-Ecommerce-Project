from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to my site")

def about(request):
    return HttpResponse("<b>This is the about section.<br>I am Haaris Saifi<br>This is my first django project</b>")

# django-admin startproject name
# django-admin startapp name / # python manage.py startapp name
# python manage.py runserver