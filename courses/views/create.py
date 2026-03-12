from django.views.generic import CreateView
from courses.models import Courses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Courses
    fields = ['title', 'content','main_image'] # Quitamos 'author' de aquí
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create_course.html'

    def test_func(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        messages.success(self.request, _("Curso Creada correctamente."))
        return super().form_valid(form)
    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request,_("Se ha producido un error al crear el curso"))
        return response