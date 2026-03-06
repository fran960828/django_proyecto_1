from django.shortcuts import render

from blog.forms import SearchForm
from blog.models import News

# Create your views here.
def news_list_view(request):
    news=News.objects.all()
    context={
        'news':news
    }
    
    return render(request,'blog/news_list.html',context)

def new_view(request,id):
    newDetail=News.objects.get(pk=id)
    context={
        'new_detail':newDetail
    }

    return render(request,'blog/new_detail.html',context)

def search_view(request):
    form = SearchForm(request.GET or None)
    # Inicializamos con un QuerySet vacío para que no cargue nada al entrar
    results = News.objects.none()
    
    # Variable para rastrear si el usuario ya intentó buscar algo
    search_performed = False

    if 'search' in request.GET:
        search_performed = True
        if form.is_valid():
            term = form.cleaned_data.get('search')
            if term:  # Solo buscamos si el término no está vacío
                results = News.objects.filter(title__icontains=term)
            # Si el término está vacío pero se envió el form, 
            # 'results' seguirá siendo .none()

    return render(request, 'blog/search.html', {
        'form': form,
        'results': results,
        'search_performed': search_performed
    })