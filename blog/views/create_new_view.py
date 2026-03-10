from django.views.generic import CreateView
from blog.models import News
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class NewsCreate(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content'] # Quitamos 'author' de aquí
    success_url = reverse_lazy('blog:news')
    template_name = 'blog/create_news.html'

    def form_valid(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        return super().form_valid(form)


    