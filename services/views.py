from django.shortcuts import render
from . import views
# Create your views here.
def django(request):
    return render(request,'django.html', {})

def scraping(request):
    return render(request,'scraping.html', {})

def automation(request):
    return render(request,'automation.html', {})