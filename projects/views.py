from django.shortcuts import render
from .models import Project

def soon(request):
    return render(request, 'soon.html', {})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
