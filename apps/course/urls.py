from django.urls import path
from .views import courses, course_detail, lesson_single

app_name = 'course'

urlpatterns = [
    path('', courses),
    path('detail/<int:pk>/', course_detail),
    path('<int:pk>/<int:pk_>/', lesson_single, name='lesson-single')
]