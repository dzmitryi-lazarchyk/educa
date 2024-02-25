from django.shortcuts import render
from django.contrib.auth import views

class MyLogoutView(views.LogoutView):
    http_method_names = ['get', 'post', 'options']
