from django.shortcuts import render

def soon(request):
    return render(request, 'soon.html', {})

def projects(request):
    return render(request, 'projects.html', {})
