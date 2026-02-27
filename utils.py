from todos.models import Student, Course,Register

student1=Student.objects.create( name='Mario')
course1=Course.objects.create(name='Django',
    code='DJ1')
course2=Course.objects.create(
    name='React',
    code='RC1'
)
register_django=Register(
    student=student1,
    course=course1,
    calification=9
)
register_django.save()
register_react=Register(
    student=student1,
    course=course2,
    calification=7
)
register_react.save()

mario_course=student1.course_set.all()