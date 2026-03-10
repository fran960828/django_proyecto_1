from django.urls import path

from courses.views import ListCourseView,DetailCourseView,CreateCourseView,UpdateCourseView,DeleteCourseView


app_name='courses'
urlpatterns = [
    path('list/',ListCourseView.as_view(),name='list'),
    path('create/',CreateCourseView.as_view(),name='create'),
    path('detail/<pk>',DetailCourseView.as_view(),name='detail'),
    path('update/<pk>',UpdateCourseView.as_view(),name='update'),
    path('delete/<pk>',DeleteCourseView.as_view(),name='delete')
]

