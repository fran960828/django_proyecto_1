
from django.urls import path
from blog.views import ListNewsView, NewDetailView,NewsCreate,NewsUpdateView,NewsDeleteView



app_name='blog'
urlpatterns = [
    path('news_list/',ListNewsView.as_view(),name='news'),
    path('news_list/<pk>',NewDetailView.as_view(),name='new_detail'),
    path('create_new/',NewsCreate.as_view(),name='create_new'),
    path('edit_new/<int:pk>/', NewsUpdateView.as_view(), name='edit_new'),
    path('delete_new/<int:pk>/', NewsDeleteView.as_view(), name='delete_new'),
]

