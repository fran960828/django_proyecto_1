from django.views.generic import CreateView
from courses.models import Courses
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CreateCourseView(LoginRequiredMixin, CreateView):
    model = Courses
    fields = ['title', 'content','main_image'] # Quitamos 'author' de aquí
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create_course.html'

    def form_valid(self, form):
        # Asignamos el autor internamente antes de guardar
        form.instance.author = self.request.user
        return super().form_valid(form)