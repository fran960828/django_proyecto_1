from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Courses

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