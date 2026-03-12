from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class DeleteCourseView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Courses
    template_name = 'courses/delete_course.html'
    success_url = reverse_lazy('courses:list')

    def test_func(self):
        # Bloquea el acceso si no es el autor ANTES de borrar
        return self.get_object().author == self.request.user

    def delete(self, request, *args, **kwargs):
        # El mensaje se genera ANTES de borrar el objeto
        messages.success(self.request, _("Curso eliminado con exito."))
        return super().delete(request, *args, **kwargs)