from django.urls import path
from . import views
urlpatterns = [
    path('django/', views.django, name='django'),
    path('scraping/', views.scraping, name='scraping'),
    path('automation/', views.automation, name='automation'),
]

