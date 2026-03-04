from django.shortcuts import render

from .models import Courses

# Create your views here.
def courses_list_view(request):
    courses=Courses.objects.all()
    context={
        'courses':courses
    }
    
    return render(request,'courses/courses_list.html',context)

def course_view(request,id):
    course_detail=Courses.objects.get(pk=id)
    context={
        'course_detail':course_detail
    }

    return render(request,'courses/course_detail.html',context)