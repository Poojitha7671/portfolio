from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def portfolio(request):
    return render(request,'portfolio.html')