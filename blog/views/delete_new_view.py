from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from blog.models import News
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class NewsDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = News
    template_name = 'blog/news_delete_form.html'
    success_url = reverse_lazy('blog:news')

    def test_func(self):
        # Bloquea el acceso si no es el autor ANTES de borrar
        return self.get_object().author == self.request.user

    def delete(self, request, *args, **kwargs):
        # El mensaje se genera ANTES de borrar el objeto
        messages.success(self.request, _("Noticia eliminada con exito."))
        return super().delete(request, *args, **kwargs)