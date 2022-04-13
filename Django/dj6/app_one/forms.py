#https://docs.djangoproject.com/en/4.0/ref/forms/widgets/#:~:text=A%20widget%20is%20Django's%20representation,DOCTYPE%20html%3E%20.
from django import forms
from .models import Email

categories = [
        ('query', 'Query'), 
        ('complaint', 'Complaint'),
        ('other', 'Other'),
        ]

colors = [('red', 'Red'), ('blue', 'Blue'), ('yellow', 'Yellow'), ('violet', 'Violet')]
gender = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
class ContactForm(forms.Form):
    name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=15, widget=forms.PasswordInput)
    email = forms.EmailField(required=False)
    category = forms.ChoiceField(choices=categories, required=False)
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea, required=False)
    fav_color = forms.MultipleChoiceField(choices=colors, widget=forms.CheckboxSelectMultiple, required=False)
    gender = forms.MultipleChoiceField(choices=gender, widget=forms.RadioSelect, required=False)

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = "__all__"
        # fields = ('sender_mail', 'subject', 'body')