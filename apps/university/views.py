from django.shortcuts import render
from apps.blog.models import Blog
from apps.course.models import Course
from django.conf import settings
from apps.accounts.models import Account
from .models import About, Service, Reason, FAQ


def home_view(request):
    courses = Course.objects.all().order_by('-id')
    teachers = Account.objects.filter(role=0).order_by('-id')[:3]
    posts = Blog.objects.order_by('-id')[:5]
    context = {
        'teachers': teachers,
        'courses': courses,
        'post': posts,
    }

    return render(request, 'index.html', context)


def about(request):
    about = About.objects.all()
    service = Service.objects.all().order_by('-id')
    reason = Reason.objects.all().order_by('-id')
    faq = FAQ.objects.all()
    context = {
        'about': about,
        'services': service,
        'reasons': reason,
        'faq': faq
    }
    return render(request, 'about.html', context)


