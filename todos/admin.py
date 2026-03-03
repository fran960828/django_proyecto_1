from django.contrib import admin
from .models import Serie,Capitulo,Director
#Parte de import-export
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CapituloInline(admin.TabularInline): # Formato tabla, más compacto
    model = Capitulo
    extra=1
    

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad') # Columnas que se verán en el listado
    search_fields = ('nombre',)    # Añade una barra de búsqueda
    

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_estreno','director') # Columnas que se verán en el listado
    search_fields = ('titulo','director__nombre') 
    list_filter= ('categoria',) 
    inlines=[CapituloInline]

#@admin.register(Capitulo)
#class CapituloAdmin(admin.ModelAdmin):
#    list_display = ('titulo', 'duracion_minutos','serie') # Columnas que se verán en el listado
#    search_fields = ('titulo',)

class CapituloResource(resources.ModelResource):
    class Meta:
        model = Capitulo
        fields = ('titulo', 'duracion_minutos','serie')  # Optional: limit fields
        export_order = ('titulo', 'duracion_minutos','serie')

# Integrate into Django admin
@admin.register(Capitulo)
class BookAdmin(ImportExportModelAdmin):
    resource_class = CapituloResource