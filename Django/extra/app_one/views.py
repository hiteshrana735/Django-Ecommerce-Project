from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def collect(request):
    name = request.GET['name']
    return render(request, 'collect.html', {'name': name})