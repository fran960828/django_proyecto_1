from django.urls import path

from .views import course_view, courses_list_view, new_course_view


app_name='courses'
urlpatterns = [
    path('courses_list/',courses_list_view,name='courses'),
    path('courses_list/new_course/',new_course_view,name='new_course'),
    path('courses_list/<int:id>',course_view,name='course_detail')
]

