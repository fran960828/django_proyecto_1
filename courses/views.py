from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Courses
from django.shortcuts import redirect
from django.urls import reverse
from .forms import CoursesForm

# Create your views here.
@login_required
def courses_list_view(request):
    courses=Courses.objects.all()
    context={
        'courses':courses
    }
    
    return render(request,'courses/courses_list.html',context)


@login_required
def course_view(request,id):
    course_detail=Courses.objects.get(pk=id)
    context={
        'course_detail':course_detail
    }

    return render(request,'courses/course_detail.html',context)

@login_required
def new_course_view(request):
    # Inicializamos el form con POST o None
    form = CoursesForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # .save() crea el objeto en la BD y lo devuelve
            nuevo_curso = form.save()
            
            # Redirección usando el nombre de la URL y el ID
            return redirect(reverse('courses:course_detail', kwargs={'id': nuevo_curso.id}))

    return render(request, 'courses/new_course.html', {'form': form})