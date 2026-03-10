
from django.views.generic import ListView
from blog.models import News

class ListNewsView(ListView):
    model = News
    template_name = "blog/news_list.html"
    context_object_name = "news"

    # Pasar información extra (ej. un título)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context