from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
]