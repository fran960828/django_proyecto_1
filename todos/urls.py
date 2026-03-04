from django.urls import path
from .views import serieView,capituloView,directorView,serie_detail_View

app_name='todos'

urlpatterns = [
    path('serie/',serieView,name='series'),
    path('capitulo/',capituloView,name='capitulos'),
    path('director/',directorView,name='directores'),
    path('serie/<int:id>',serie_detail_View,name='serieDetail')
]