
from django.contrib import admin
from .models import Courses 

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    # 1. Columnas que se verán en el listado principal
    list_display = ('title', 'date_creation', 'show_course',)
    
    # 6. Orden predeterminado (de más reciente a más antiguo)
    ordering = ('-date_creation',)