from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from courses.models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin

class DeleteCourseView(LoginRequiredMixin,DeleteView):
    model = Courses
    template_name = 'courses/delete_course.html'
    success_url = reverse_lazy('courses:list')