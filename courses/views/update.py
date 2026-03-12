from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class UpdateCourseView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Courses
    fields = ['title', 'content'] # Normalmente no dejamos editar el autor
    template_name = 'courses/update_course.html' # Puedes reutilizar el de creación si quieres
    success_url = reverse_lazy('courses:list')

    def test_func(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        messages.success(self.request, _("Curso actualizado correctamente."))
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,_("Se ha producido un error al actualizar el curso"))
        return response