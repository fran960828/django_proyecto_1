from django.shortcuts import render

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