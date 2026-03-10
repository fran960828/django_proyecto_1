from django.views.generic import TemplateView
from courses.models import Courses
from blog.models import News

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        # 1. Obtenemos el contexto base
        context = super().get_context_data(**kwargs)
        
        # 2. Query para Cursos (ej: los 3 más recientes)
        context['courses'] = Courses.objects.filter(show_course=True).order_by('-date_creation')[:2]
        
        # 3. Query para Artículos de Blog (ej: los 4 últimos)
        context['news'] = News.objects.filter(show_news=True).order_by('-date_creation')[:2]
        
        return context