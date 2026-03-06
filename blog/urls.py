from django.urls import path

from blog.views import new_view, news_list_view, search_view


app_name='blog'
urlpatterns = [
    path('news_list/',news_list_view,name='news'),
    path('news_list/<int:id>',new_view,name='new_detail'),
    path('search/',search_view,name='search')
]

