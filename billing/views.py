from django.shortcuts import render, HttpResponse, redirect
from .models import Coffee

# Create your views here.

def home(request):
    coffee = Coffee.objects.all()
    return render(request, 'home.html', {'coffee':coffee})
