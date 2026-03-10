from blog.models import News
from django.views.generic import DetailView

class NewDetailView(DetailView):
    model = News # Especificamos el modelo
    template_name = "blog/new_detail.html"
    context_object_name='new_detail'