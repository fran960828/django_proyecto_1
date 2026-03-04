
from django.shortcuts import render

def homeView(request):
    
    return render(request,'general/home.html')

def aboutView(request):
    
    return render(request,'general/aboutUs.html')