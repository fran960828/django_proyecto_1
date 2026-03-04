from django.shortcuts import render
from ..models import Serie

def serie_detail_View(request,id):
    serie=Serie.objects.get(pk=id)
    context={
        'info_serie': serie,
    }
    
    return render(request,'todos/serie_detail.html',context)