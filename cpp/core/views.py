from django.shortcuts import render
from django.http import request
# Create your views here.

def home(request):
    return render(request, 'core/home.html', {})

def rol(request):
    return render(request, 'core/rol.html', {})

def permiso(request):
    return render(request, 'core/permiso.html', {})
