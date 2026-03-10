from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdateCourseView(LoginRequiredMixin,UpdateView):
    model = Courses
    fields = ['title', 'content'] # Normalmente no dejamos editar el autor
    template_name = 'courses/update_course.html' # Puedes reutilizar el de creación si quieres
    success_url = reverse_lazy('courses:list')