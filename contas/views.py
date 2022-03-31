from django.shortcuts import render
from django.http import HttpResponse
import datetime

def home(request):
    return render(request, 'contas/home.html')