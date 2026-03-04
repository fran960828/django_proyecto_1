from django.shortcuts import render
from ..models import Serie

def serieView(request):
    series=Serie.objects.all()
    context={
        'lista_series': series,
        'encabezado':'Catalogo de series 2026'
    }
    
    return render(request,'todos/series.html',context)