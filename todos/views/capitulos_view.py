from django.shortcuts import render

def capituloView(request):
    
    return render(request,'todos/capitulos.html')