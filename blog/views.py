from django.shortcuts import render, get_object_or_404
from .models import Project


def all_blogs(request):
    projects = Project.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'projects': projects})


def detail(request, blog_id):
    blog = get_object_or_404(Project, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})