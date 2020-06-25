from django.urls import path

from profiles_api import views

url_patterns = [
    path('hello-view/',views.HelloApiView.as_view())
]