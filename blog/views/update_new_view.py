from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from blog.models import News
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class NewsUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = News
    fields = ['title', 'content'] # Normalmente no dejamos editar el autor
    template_name = 'blog/news_update_form.html' # Puedes reutilizar el de creación si quieres
    success_url = reverse_lazy('blog:news')

    def test_func(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        messages.success(self.request, _("Noticia actualizada correctamente."))
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,_("Se ha producido un error al actualizar la noticia"))
        return response