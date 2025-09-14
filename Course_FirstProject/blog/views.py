from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'blog/index.html', context={'site': 'mysite.com'})


def contact(request):
    return redirect('blog:about')


def about(request):
    return render(request, 'blog/about.html', context={'site': 'Stepik'})
