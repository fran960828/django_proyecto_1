from django.contrib import admin
from .models import News 

@admin.register(News)
class NoticiaAdmin(admin.ModelAdmin):
    # 1. Columnas que se verán en el listado principal
    list_display = ('title', 'author', 'date_creation', 'show_news',)
    
    # 6. Orden predeterminado (de más reciente a más antiguo)
    ordering = ('-date_creation',)

   