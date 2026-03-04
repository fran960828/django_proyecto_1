from django.shortcuts import render

def directorView(request):
    
    return render(request,'todos/directores.html')