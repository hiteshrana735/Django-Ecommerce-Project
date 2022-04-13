from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def form(request):
    if request.method == 'POST':
        username = request.POST['nm']
        email = request.POST['usermail']
        context = {
            'name': username, 
            'mail': email
        }
        return render(request, 'form.html', context)
    else: 
        return render(request, 'form.html')

# Word Counter ->   