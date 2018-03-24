from django.urls import path

from . import views

urlpatterns = [
    path('myfunction', views.index, name='index'),
]