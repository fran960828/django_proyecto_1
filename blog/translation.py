from modeltranslation.translator import register, TranslationOptions
from .models import News

# Registramos el modelo Curso con sus opciones de traducción
@register(News)
class CourseTranslationOptions(TranslationOptions):
    # Definimos los campos que tendrán versiones en varios idiomas
    fields = ('title', 'content')