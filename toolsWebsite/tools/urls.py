from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('init', views.init, name='init'),
    path('available', views.availableTools, name='available'),
]
