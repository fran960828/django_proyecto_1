from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from blog.models import News

class NewsUpdateView(UpdateView):
    model = News
    fields = ['title', 'content'] # Normalmente no dejamos editar el autor
    template_name = 'blog/news_update_form.html' # Puedes reutilizar el de creación si quieres
    success_url = reverse_lazy('blog:news')