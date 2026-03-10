from courses.models import Courses
from django.views.generic import DetailView

class DetailCourseView(DetailView):
    model = Courses # Especificamos el modelo
    template_name = "courses/detail_course.html"
    context_object_name='detail'