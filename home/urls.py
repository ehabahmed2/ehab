from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact_form'),
    path('questions/', views.questions, name='questions'),
]