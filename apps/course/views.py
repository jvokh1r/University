from django.shortcuts import render
from .models import Course, CourseDetail, Lesson


def courses(request):
    course = Course.objects.all()

    context = {
        'courses': course,
    }
    return render(request, 'courses.html', context)


def course_detail(request, pk):
    if pk is not None:
        post = CourseDetail.objects.get(id=pk)
        l = Lesson.objects.filter(course_id=pk)
    context = {
        'courses': post,
        'lessons': l
    }
    return render(request, 'course-single.html', context)


def lesson_single(request, pk, pk_):
    lesson = Lesson.objects.filter(course_id=pk).get(id=pk_)
    context = {
        'lessons': lesson,
    }
    return render(request, 'lesson.html', context)


