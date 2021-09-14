from django.urls import path

from . import views
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('temp', views.temp, name='temp'),
    path('list', views.list, name='list'),
]
