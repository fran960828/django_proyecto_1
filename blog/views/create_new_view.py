from django.views.generic import CreateView
from blog.models import News
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class NewsCreate(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'content'] # Quitamos 'author' de aquí
    success_url = reverse_lazy('blog:news')
    template_name = 'blog/create_news.html'

    def form_valid(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        messages.success(self.request, _("Noticia creada correctamente."))
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,_("Se ha producido un error al crear la noticia"))
        return response


    