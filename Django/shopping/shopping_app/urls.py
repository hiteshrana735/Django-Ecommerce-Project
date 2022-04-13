from django.contrib import admin
from django.urls import path
from .views import CartAPI

urlpatterns = [
    path('cart/', CartAPI.as_view()),
    path('cart/<int:id>', CartAPI.as_view()),
]
