from django.contrib import admin
from app_one.models import LoginDetails, Email

# Register your models here.
admin.site.register([LoginDetails, Email])