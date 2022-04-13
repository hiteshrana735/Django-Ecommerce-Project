from django.shortcuts import render
from .forms import ContactForm, EmailForm
from .models import LoginDetails

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Bound form
        form = ContactForm(request.POST)
        if form.is_valid():
            form_name = form.cleaned_data['name']
            form_password = form.cleaned_data['password']
            # print(name, password)
            login = LoginDetails(name=form_name, password=form_password)
            login.save()

    # unbound form
    form = ContactForm()
    return render(request, 'index.html', {'form_one':form})
    

def email(request):
    form = EmailForm()
    return render(request, 'emailform.html', {'form_two':form})
