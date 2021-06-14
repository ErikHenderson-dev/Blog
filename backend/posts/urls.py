from django.urls import path
from . import views

urlspatters = {
    path('', views, name='index'),
    path('', views, name='show'),
}