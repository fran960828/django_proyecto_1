from django.views.generic import ListView
from courses.models import Courses

class ListCourseView(ListView):
    model = Courses
    template_name = "courses/list_courses.html"
    context_object_name = "list"