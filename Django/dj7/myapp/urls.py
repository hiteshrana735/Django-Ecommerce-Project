from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('show', views.show, name='show'),
    path('login/', views.login, name='login'),
    path('dashboard', views.dash, name='dashboard'),
    path('logout', views.logout, name='logout'),
]